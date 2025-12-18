# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 2021

@author: 
"""
import numpy as np
import random

def put_cards(n: int):
    # Cria a matriz com as cartelas dos bingos
    list_cards_bing = [] # Lista vazia
    # print(cards_bing)
    i = int(0)
    for i in range(0, n*6):
        j = int(0)
        print("Digite o elemento (", j, ",", i%6, ")")
        aux = int(input())
        list_cards_bing.append(aux)
        if j == 6:
            j = 0
        else:
            j = j+1
    
    # Converte a lista em uma matriz (n, 6)
    cards_bing = np.array(list_cards_bing).reshape(-1,6)
             
    return cards_bing

def change_for_zero(a: np, number:int):
    # Troca todos os números iguais a number por 0
    a[a == number] = 0
    # return a

def check_win(a: np):
    # Verifica se alguma linha é 0
    check = False
    result = np.all((a == 0), axis=1)
    for i in range(len(result)):
        if(result[i]):
            print("CONGRATULAÇÕES!")
            print("PELO MENOS UMA PESSOA GANHOU O SORTEIO!")
            print("Cartela vencedora: ", i)
            print("\n")
            check = True
    return check

def remove_duplicate(my_list:list):
    # Remove os elementos duplicados de uma lista
    final_list = []
    for num in my_list:
        if num not in final_list:
            final_list.append(num)
    return final_list


def main():
    lst_sort_number = []
    result_win = False
    
    N = int(input("Digite o número N de cartelas: "))
    
    # Criando a matriz de tamanho Nx6
    print("Digite os ", N*6, " valores (entre 1 e 60):")
    
    # Preenchedo as cartelas
    cards_bing = put_cards(N)
    print("\n")
    
    c_continue = int(1)
    while (c_continue == 1): 
        
        number = random.randint(1, 60)
        print("ATENÇÃO: Número do sorteio:", number)
        print("\n")
        lst_sort_number.append(number)
        
        # Trocando todos os números
        change_for_zero(cards_bing, number)
        
        # Verificando se alguém venceu
        result_win = check_win(cards_bing)
        
        if result_win == True:
            print("Alguém ganhou. Digite 0 e encerre o bingo.")
        else:
            print("Ninguém ganhou. Digite 1 e sorteie um novo número.\n")
        
        print("***Cartelas***") # Zero indica que o número foi sorteado
        print(cards_bing)
        
        c_continue = int(input("Continuar? (1-Sim/0-Não):"))
        print("\n")
    
    #print(lst_sort_number)
    #print("\n")
    print("Números sorteados (sem repetição, na ordem em que foram sorteados e não ordenados):")
    print(remove_duplicate(lst_sort_number))
        
        
    

# Chama quando lista_1.py é executada como main
if __name__ == '__main__':
    main()
