from math import exp
from tree import arbol

def binomial(S,K,T,r,u,d,n,put=False,am=True):
    """
    Argumentos:
        S (número): So ---> Valor de la acción
        K (número): Precio de ejercicio
        T (número): Total de periodos
        r (número): TLR ---> Tasa libre de riesgo
        u (número): Probabilidad de que suba
        d (número): Probabilidad de que baje
        n (número): Total de periodos
    Returns:
        [lista]: [Precios]
    """
    t=T/n  # tiempo entre cada periodo 
    p=(exp(r*t)-d)/(u-d)    # -----> probabilidad p
    lista=[];valores=[]
    pos=-1 if put==True else 1
    for m in range(n+1):
        st=S*(u**(m))*(d**(n-m)) 
        valores.append(max(pos*(st-K),0)) # Necesitamos solo los del ultimo periodo para empezar desde el ultimo y terminar en el P0 o C0 segun sea el caso
        for i in range(m+1):  # Aqui si necesitamos todos los valores para cada nodo
            st=S*(u**(m-i))*(d**i)
            if n<10: lista.append(f's0*u^{m-i}(d^{i})={round(st,2)}')
            elif n>=10: lista.append(round(st,2))
            elif n>=38: lista.append(round(st,1))
    for k in range(n-1,-1,-1): # conteo que va desde N-1,N-2,N-3...0 
        for i in range(k+1):
            if am: valores[i]=max(pos*(S*u**i*d**(k-i)-K),exp(-r*t)*(p*valores[i+1]+(1-p)*valores[i]))
            else: valores[i]=exp(-r*t)*(p*valores[i+1]+(1-p)*valores[i]) # valores de la opcion segun el periodo
    if put:            # Si se analiza bien, este if sale sombrando por la paridad call-put
        put=valores[0]
        call=put-K*exp(-r*T)+S
        if am:
            print(f"Valor del call AMERICANO ==== {call}")
            print(f"Valor del put AMERICANO ==== {put}")
        else:
            print(f"Paridad call-put ------------------------> {put+S} = {call+K*exp(-r*T)}")
            print(f"Valor del call ==== {call}")
            print(f"Valor del put  ==== {put}")
    else:  
        call=valores[0]
        put=call+K*exp(-r*T)-S
        print(f"Paridad call-put ------------------------> {put+S} = {call+K*exp(-r*T)}")
        print(f"Valor del call ==== {call}")
        print(f"Valor del put  ==== {put}")
    return lista
N=20;S=50;K=51;T=6/12;r=0.05;u=1.06;d=0.95 # Ejemplo
fn=binomial(S,K,T,r,u,d,N,put=False,am=False)
arbol(N,fn)
