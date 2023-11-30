# nessuscombiner
Combine Nessus DB files to compile them into a single *.Nessus file for ease of review

## Getting Started

```normal
git clone https://github.com/smhuda/nessuscombiner.git
cd nessuscombiner
```
## Usage
To use this tool, run the script with the directory path as an input:
```normal
python nessuscombiner.py
```
> ℹ️ **Place all .nessus files in the same directory as the nessuscombiner.py is placed at**

### Example 

```normal
├─ nessuscombiner/
│  ├─ scan-1.nessus
│  ├─ scan-2.nessus
│  ├─ scan-3.nessus
│  ├─ nessuscombiner.py
```
This should generate a `combined.nessus` file with all combined Nessus files into one.

## Contributing
Contributions, issues, and feature requests are welcome! 

If you liked this or if it helped you in any way

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/smhuda)
