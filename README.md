# spark.py

Print sparks like ▁▂▃▅▂▇ in your shell or use it in your python projects

## Usage

spark.py VALUE [,] ...

## Examples
```spark.py 1 5 22 13 53
	▁▁▃▂█
	spark.py 1.2 5.5 22.9 13.2 53.3
	▁▁▃▂█
	spark.py 0,30,55,80,33,150
	▁▂▃▄▂.█
	echo 9 13 5 17 1 | spark.py
	▄▆▂█▁
```

```from spark import getSparks
	print getSparks([1, 5, 22, 13, 53])
```

# Thanks to
 
Idea from Zach Holman @ https://github.com/holman/spark