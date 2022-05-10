# ignores-to-dotsnyk

This CLI project allows Snyk customers to generate a .snyk file for issues they have ignored in the Snyk UI. More on the .snyk file [here](https://docs.snyk.io/snyk-cli/test-for-vulnerabilities/the-.snyk-file).

## Requirements
 - \>= Python 3.8
 - pip

## Instructions

### Setup
1. Clone this project onto your local machine.
2. From the project root run `pip install .`
3. You may need to add your python installation to your PATH
    - `cd ~`
    - `vi .zshrc` or `vi .bash_profile`
    - add `export PATH=$PATH:<path/to/your/python>/bin`

### Running the CLI
```
ignores-to-dotsnyk \
-o <YOUR_ORGANIZATION_ID> \
-p <YOUR_PROJECT_ID> \
-a <YOUR_API_KEY> \
-d <OUTPUT_DIRECTORY>
```
Note: `-d` is optional. If omitted, the .snyk file will be output in the current working directory.
