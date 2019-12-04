all: resultado.png sigma.png solar.png

solar.png: sol.dat fourier.py
	python fourier.py
sigma.png: valores.txt metropolis.py
	python metropolis.py
resultado.png : ecuacion.dat ecuacion.py
	python ecuacion.py

ecuacion.dat:ecuacion.x
	./ecuacion.x > ecuacion.dat

ecuacion.x : ecuacion.cpp
	c++ ecuacion.cpp -o ecuacion.x