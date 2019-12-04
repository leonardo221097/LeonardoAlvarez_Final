  
#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

// para realizar este ejercicio modifiqué el codigo entregado en el ejercicio 32 de la clase
int main(){
	// condiciones iniciale dadas en el libro y dadas en clase

float deltat = 0.01;
float deltax = 0.01;
float t= 0.5;
float L = 2.0;
int numt = t/deltat;
int numx= L/deltax;



    //creo la matriz
    double **M = new double *[numx];
    for (int i=0;i<numx;i++){
        M[i] =new double[numt];
    }
    
  for (int j=1;j<numx-1;j++)
    {
       M[0][j] = exp(-0.5*((pow((L-1),2))/pow(0.25,2)));
    }
       
		
        
    
    //lleno la matriz.
    for(int i=1;i<numt-1;i++){
        for(int j=1; j<numx-1; j++){
            M[i][j+1] =((M[i+1][j]-M[i-1][j])/deltat)+ (((M[i][j+1]-M[i][j-1]))/deltax);
        }
    }
     // imprimo los valores de la matriz en un .dat
    ofstream outfile;
outfile.open("ecuacion.dat");
    for(int i=0; i<numt; i++){
        for(int j=0; j<numx; j++){
            outfile<<M[i][j]<<"\t";
        }
        outfile<<endl;
    }
    outfile.close();
    
    
    return 0;
}