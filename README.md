    # Python Environment comparator(PEC)

### PEC supports comparision of two virtual environemnts.

## How to run:
```python
from env_comparator.compare import Compare

if __name__ == '__main__':
    data = Compare("requirements_env1.txt", "requirements_env3.txt")
    data.get_status()

```
## Output:
```python
---------------------------------------------------------------------------------------------------------------
|file1 :requirements_env1.txt         |file2 :requirements_env3.txt         | is subset :False                |
---------------------------------------------------------------------------------------------------------------
|           Package            |    requirements_env1.txt     |    requirements_env3.txt     |     Status     |
---------------------------------------------------------------------------------------------------------------
|contourpy                     |1.0.7                         |1.0.6                         |Version Mismatch|
|cycler                        |0.11.0                        |0.11.0                        |OK              |
|fonttools                     |4.38.0                        |4.38.0                        |OK              |
|kiwisolver                    |1.4.4                         |1.4.4                         |OK              |
|matplotlib                    |3.6.2                         |3.6.2                         |OK              |
|numpy                         |1.23.5                        |1.23.5                        |OK              |
|packaging                     |21.3                          |21.3                          |OK              |
|pandas                        |1.5.1                         |1.5.1                         |OK              |
|pillow                        |9.3.0                         |9.3.0                         |OK              |
|pyparsing                     |3.0.9                         |3.0.9                         |OK              |
|python-dateutil               |2.8.2                         |2.8.2                         |OK              |
|pytz                          |2022.6                        |2022.6                        |OK              |
|scipy                         |1.9.3                         |1.9.3                         |OK              |
|seaborn                       |0.10.1                        |0.10.1                        |OK              |
|six                           |1.16.0                        |Missing                       |Not OK          |
---------------------------------------------------------------------------------------------------------------
```