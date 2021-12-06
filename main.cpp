#include <iostream>
#include<math.h>

using namespace std;

int radio,xP, yP, xC, yC;
void findPoint();


void findPoint(){

    int x,y, cuadradoX, cuadradoY, distancia, cuadradoR;

    //Estamos la coordenada en X del punto con la coordenada en X del Centro
    x=(xP-xC);
    //Estamos la coordenada en Y del punto con la coordenada en Y del Centro
    y=(yP-yC);

    //Elevamos el radio al cuadrado
    cuadradoR = pow(radio,2);

    //Elevamos cuadrado la resta de xP - xC
    cuadradoX = pow(x,2);
    //Elevamos cuadrado la resta de yP - yC
    cuadradoY = pow(y,2);

    //Para obtener la distancia sumamos lo obtenido con cuadradoX y cuadradoY
    distancia = cuadradoX + cuadradoY;


    //Posibles resultados
    if(distancia > cuadradoR ){
        cout<<"El punto esta fuera del circulo"<<endl;
    } if (distancia < cuadradoR){
        cout<<"El punto esta dentro del circulo"<<endl;
    } if(distancia == cuadradoR){
        cout<<"El punto en el circulo"<<endl;
    }

}


int main() {

    //Pedimos los datos

    cout<<"Ingresa el radio del circulo"<<endl;
    cin>>radio;
    cout<<"Ingresa la coordenada en X para el punto"<<endl;
    cin>>xP;
    cout<<"Ingresa la coordenada en Y para el punto"<<endl;
    cin>>yP;
    cout<<"Ingresa la coordenada en X para el centro del circulo"<<endl;
    cin>>xC;
    cout<<"Ingresa la coordenada en Y para el centro del circulo"<<endl;
    cin>>yC;

    findPoint();

    return 0;


}
