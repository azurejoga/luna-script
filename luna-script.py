import wx
import os
import requests
import threading
import zipfile
from io import BytesIO

class LunaDownloader(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Luna Downloader", size=(400, 300))
        self.panel = wx.Panel(self)

        self.listBox = wx.ListBox(self.panel, size=(300, 200), pos=(40, 20))
        self.buttonDownload = wx.Button(self.panel, label="Download", size=(80, 30), pos=(160, 240))

        self.Bind(wx.EVT_BUTTON, self.on_download_click, self.buttonDownload)

        # JSON link (replace with your actual link)
        self.json_url = "https://github.com/azurejoga/luna-script/raw/master/luna.json"
        self.json_content = self.download_json_content()

        # Add versions to the list box
        if self.json_content is not None:
            for version in self.json_content:
                self.listBox.Append(version['name'])

    def download_json_content(self):
        try:
            response = requests.get(self.json_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            wx.LogError(f"Error downloading JSON content: {e}")
            return None

    def on_download_click(self, event):
        selected_item = self.listBox.GetStringSelection()

        if selected_item:
            selected_version = next((version for version in self.json_content if version['name'] == selected_item), None)

            if selected_version:
                default_download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
                save_dialog = wx.FileDialog(self, "Save file", defaultDir=default_download_path, style=wx.FD_SAVE)

                if save_dialog.ShowModal() == wx.ID_OK:
                    save_path = save_dialog.GetPath()
                    progress_frame = ProgressFrame(self, selected_version['url'], save_path)
                    progress_frame.Show()


class ProgressFrame(wx.Frame):
    def __init__(self, parent, download_url, save_path):
        wx.Frame.__init__(self, parent, title="Downloading...", size=(300, 100))
        self.panel = wx.Panel(self)

        self.progress_bar = wx.Gauge(self.panel, range=100, size=(250, -1), pos=(20, 40))
        self.label_downloading = wx.StaticText(self.panel, label="Downloading, please wait...", pos=(20, 20))

        self.download_url = download_url
        self.save_path = save_path

        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.download_thread = threading.Thread(target=self.start_download_and_extract)
        self.download_thread.start()

    def start_download_and_extract(self):
        try:
            response = requests.get(self.download_url, stream=True)
            response.raise_for_status()

            with open(self.save_path, 'wb') as file:
                total_size = int(response.headers.get('content-length', 0))
                block_size = 1024
                downloaded = 0

                for data in response.iter_content(block_size):
                    file.write(data)
                    downloaded += len(data)
                    progress = int((downloaded / total_size) * 100)
                    wx.CallAfter(self.update_progress, progress)

            extension = os.path.splitext(self.save_path)[1].lower()

            if extension in {'.zip', '.rar', '.7z'}:
                wx.CallAfter(self.update_message, "Extracting, please wait...")
                wx.CallAfter(self.extract_archive)

        except requests.exceptions.RequestException as e:
            wx.CallAfter(wx.LogError, f"Error downloading content: {e}")

        finally:
            wx.CallAfter(self.Close)

    def update_progress(self, value):
        wx.CallAfter(self.progress_bar.SetValue, value)

    def update_message(self, message):
        wx.CallAfter(self.label_downloading.SetLabel, message)

    def extract_archive(self):
        try:
            with zipfile.ZipFile(self.save_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(self.save_path))
            wx.CallAfter(wx.MessageBox, "Extraction complete", "Extraction Complete", wx.OK | wx.ICON_INFORMATION)
        except zipfile.BadZipFile:
            wx.CallAfter(wx.LogError, "Error extracting archive: Invalid ZIP file")

    def on_close(self, event):
        if self.download_thread.is_alive():
            wx.LogError("Download is in progress. Please wait for it to complete.")
        else:
            self.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    frame = LunaDownloader()
    frame.Show()
    app.MainLoop()
