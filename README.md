## FreeType Regression Testing scripts

This repo contains scripts used for testing regressions in FreeType.

## Usage
The script checks a "base" version of freetype vs a "test" version.

Follow these steps to test freetype

1. Build and install `ft-demos` linked with the "base" version of FreeType.
2. Call `./gen_base.sh`
3. Build and install `ft-demos` linked with the "test" version of FreeType.
4. Call `./regression.sh`
5. If regressions are found,  
 the script generates a file `"report.tar.gz"`  
 that contains webpages to browse the list of regressions.

## Configuration
The following environment variables can be used to configure the script:
- `FTT_BASE_TOOLS_DIR`: Location of base `ft-demos binaries` (ftlint, ftgrid, etc)
  - `/usr/local/bin` by default

- `FTT_TEST_TOOLS_DIR`: Location of test `ft-demos` binaries (ftlint, ftgrid, etc)
  - `/usr/local/bin` by default

- `FTT_BASE_OUTPUT_DIR`: Where the `gen_base.sh` output is stored.
  - `base/` folder inside the repo by default

- `FTT_TEST_OUTPUT_DIR`: Where the `regression.sh` output is stored.
  - `test/` folder inside the repo by default

## CAUTION: The scripts erase the contents of the output folders,<br /> so be careful not to store important data in those directories.

- The scripts look for fonts inside the `fonts/` folder,   
if you want to add/remove a font,\ simply add/remove its font file there.

- The font sizes to generate/test  
 are located in an array `fontsize_array` in both scripts,  
it can be used to configure which font sizes should be tested.
