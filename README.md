# Luna Script

## Overview

Luna Script is an all-encompassing Python application, powered by the wxPython library, designed with meticulous care to simplify the version management and download process for various applications and games. Its sophisticated yet user-friendly interface empowers users to effortlessly navigate through different versions, providing a seamless and visually appealing experience.

## Key Features
   
### 1. **Intuitive User Interface**

   Luna Script boasts a visually stunning and intuitive graphical interface, courtesy of the wxPython library. The design prioritizes user experience, making it easy for individuals of all technical levels to interact seamlessly with the application.

### 2. **Advanced Version Management**

   Effortlessly stay up-to-date with the latest releases. Luna Script retrieves detailed version information using the `requests` library, parsing JSON responses for easy updates and additions of new versions. This ensures users always have access to the most recent software versions.

### 3. **Efficient Download Functionality**

   Luna Script streamlines the download process for specific application versions, utilizing the `requests` library for efficient HTTP requests. Users can simply select the desired version and initiate the download with a click. A progress bar visually indicates the download status, ensuring transparency and confidence in the process.

### 4. **Multithreading for Enhanced Performance**

   Leveraging the power of threading (`treading`), Luna Script ensures a smooth and responsive user experience during downloads. This enables users to continue exploring the interface and performing other tasks without interruptions.

### 5. **Dynamic Extraction of ZIP Files**

   Luna Script doesn't stop at downloads; it goes the extra mile by intelligently extracting ZIP files using the `zipfile` library. If a downloaded file is a ZIP archive, Luna Script automatically unpacks its contents, providing users with ready-to-use applications or games.

### 6. **Customizable Configuration with JSON**

   Tailor Luna Script to your needs using a JSON file for version specification. This flexibility enables users to customize and configure the application according to their preferences, making it adaptable to various use cases.

### 7. **Convenient Test Example Included**

   Luna Script comes pre-loaded with a test example. A link to a JSON file is provided directly within the `script.py` file, offering a convenient test scenario for users to explore the application's features. The JSON example can be found [here](https://github.com/azurejoga/luna-script/blob/master/luna.json).

## Installation

1. **Clone the Repository:**

   ```git
   git clone https://github.com/azurejoga/luna-script.git
   ```

2. **Install Dependencies:**

   ```pip
   pip install wxpython
   pip install requests
   ```

3. **Run the Application:**

   ```cmd
   cd luna-script
   python luna-script.py
   ```

## How to Use

1. **Select Desired Version:**

   - Navigate through the user-friendly interface to choose the specific version of the application or game you wish to download.

2. **Initiate Download:**

   - Click the "Download" button to commence the download process. Track the progress visually through the provided status bar.

3. **Choose Download Location:**

   - Luna Script provides an intuitive window for selecting the download location, ensuring flexibility and convenience.

4. **Explore Luna Script:**

   - Enjoy the downloaded version, appreciating the seamless experience facilitated by Luna Script.

## Contributions and License

We want to add support for
* extraction rar, 7z etc...
* Description, tags, among other JSON parameters to improve the visibility of installed applications
* Add the possibility of personalized instructions, such as automatically executing .bat, .exe files and others
Then
Contributions to Luna Script are highly encouraged! Whether you are contributing code, reporting issues, or suggesting improvements, your input is valuable. Luna Script is licensed under the GPL License, providing a foundation for collaborative development.

Feel free to explore, contribute, and customize Luna Script to meet your specific requirements!
