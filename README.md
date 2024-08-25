# Generate FNT and Textures Tool

This tool is designed to generate a `.fnt` file and a corresponding `.png` sprite sheet from individual images in a specified input folder. It is particularly useful for game development, where you need to consolidate multiple images into a single texture atlas.

## Features

- Combines individual images into a single sprite sheet.
- Generates a `.fnt` file containing metadata for use in game engines.
- Supports customizable output image dimensions.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

Clone this repository and install the required packages using pip:

```bash
git clone https://github.com/xxeye/generate-fnt-tool.git
cd your-repo-name
pip install -r requirements.txt
```

## Usage

Here is a detailed guide on how to use the "generate_fnt_and_imageV2" tool:

### Step 1: Prepare Original Images

- Rename your original images according to the ASCII encoding rules.
- Ensure all images are stored in a single folder. The name of this folder will be used as the name of the output `.fnt` file and `.png` sprite sheet.


![image](https://github.com/xxeye/generate-fnt-tool/blob/main/image/Pasted%20image%2020240521141742.png)


Character | ASCII Code | Character | ASCII Code | Character | ASCII Code
----------|------------|-----------|------------|-----------|------------
      !   | 33         |    "      | 34         |    #      | 35
      $   | 36         |    %      | 37         |    &      | 38
      '   | 39         |    (      | 40         |    )      | 41
      *   | 42         |    +      | 43         |    ,      | 44
      -   | 45         |    .      | 46         |    /      | 47
      0   | 48         |    1      | 49         |    2      | 50
      3   | 51         |    4      | 52         |    5      | 53
      6   | 54         |    7      | 55         |    8      | 56
      9   | 57         |    :      | 58         |    ;      | 59
      <   | 60         |    =      | 61         |    >      | 62
      ?   | 63         |    @      | 64         |    A      | 65
      B   | 66         |    C      | 67         |    D      | 68
      E   | 69         |    F      | 70         |    G      | 71
      H   | 72         |    I      | 73         |    J      | 74
      K   | 75         |    L      | 76         |    M      | 77
      N   | 78         |    O      | 79         |    P      | 80
      Q   | 81         |    R      | 82         |    S      | 83
      T   | 84         |    U      | 85         |    V      | 86
      W   | 87         |    X      | 88         |    Y      | 89
      Z   | 90         |    [      | 91         |    \      | 92
      ]   | 93         |    ^      | 94         |    _      | 95
      `   | 96         |    a      | 97         |    b      | 98
      c   | 99         |    d      | 100        |    e      | 101
      f   | 102        |    g      | 103        |    h      | 104
      i   | 105        |    j      | 106        |    k      | 107
      l   | 108        |    m      | 109        |    n      | 110
      o   | 111        |    p      | 112        |    q      | 113
      r   | 114        |    s      | 115        |    t      | 116
      u   | 117        |    v      | 118        |    w      | 119
      x   | 120        |    y      | 121        |    z      | 122
      {   | 123        |    \`|\`  | 124        |    }      | 125
      ~   | 126        |           |            |           | 


### Step 2: Select Input Folder

- Launch the `generate_fnt_and_imageV2.exe` application.
- In the application, click the "Browse" button to select the folder containing the renamed images.

![image](https://github.com/xxeye/generate-fnt-tool/blob/main/image/Pasted%20image%2020240521141822.png)

### Step 3: Select Output Folder

- Choose a folder where the generated `.fnt` file and `.png` image will be saved. You can choose a different location from the input folder.

![image](https://github.com/xxeye/generate-fnt-tool/blob/main/image/Pasted%20image%2020240521141841.png)

### Step 4: Input Image Size

- Enter the desired image size in the prompt provided by the application. This will determine the size of the generated `.png` image.

![image](https://github.com/xxeye/generate-fnt-tool/blob/main/image/Pasted%20image%2020240521141905.png)

### Step 5: Generate Files

- After confirming all settings, click the "OK" button to start generating the `.fnt` file and `.png` image.
- When you see the "Done!" message, the font file and image have been successfully generated.

![image](https://github.com/xxeye/generate-fnt-tool/blob/main/image/Pasted%20image%2020240521141954.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

If you have any questions or issues, please feel free to open an Issue to discuss them.