from numpy import random
from questions import Preguntas


class Question:
    def __init__(self, prompt):
        self.prompt = prompt['Q']
        self.options = f" (a) {prompt['A']}\n (b) {prompt['B']}\n (c) {prompt['C']}\n (d) {prompt['D']}\n"
        self.answer = prompt['R']


def run_test():
    preguntas = Preguntas()
    question1 = random.randint(0,5)
    question2 = random.randint(0,5)
    question3 = random.randint(0,5)
    question4 = random.randint(0,5)
    question5 = random.randint(0,5)

    # print(question1)
    # print(question2)
    # print(question3)
    # print(question4)
    # print(question5)
    
    
    questions = [
        Question(preguntas.nivel1[question1]),
        Question(preguntas.nivel2[question2]),
        Question(preguntas.nivel3[question3]),
        Question(preguntas.nivel4[question4]),
        Question(preguntas.nivel5[question5]),
    ]
    
    score = 0
    prize = 0
    
    print("""
          *********************************************************
          ----BIENVENIDOS AL CONCURSO DE PREGUNTAS Y RESPUESTAS----
          
          Por favor seleccione "a", "b", "c" o "d" para responder.
          Son 5 niveles, cada pregunta tiene cierto valor, si se 
          responde correctamente podrá pasar a la siguiente ronda, 
          sino perderá todo el valor que haya acumulado. Si decide 
          retirarse de manera voluntaria podrá quedarse con el
          valor acumulado hasta el momento.
          
                                Valor Acumulado
          Nivel 1: 3 millones de epesos
          Nivel 2: 9 millones de pesos
          Nivel 3: 27 millones de pesos
          Nivel 4: 91 millones de pesos
          Nivel 5: 273 millones de pesos
          
          Si desea renunciar en cualquier momento escriba "salir".
          *********************************************************
          """)
    
    for question in questions:
        print("")
        print("Escriba 'a', 'b', 'c' o 'd' // Si decide retirarse escriba 'salir'")
        print(question.prompt)
        print(question.options)
        answer = input()
        if answer.lower() == question.answer.lower():
            score += 1
            prize = 3**score
        elif answer.lower() == "salir":
            print("")
            print("Has decidido retirarte del juego")
            print("Obtuviste " + str(score) + "/" + str(len(questions)) + " correctas")
            print("Has ganado " + str(prize) + " millones de pesos!")
            return None
        else:
            print(" Has perdido :C ")
            return None
            
    print("Obtuviste " + str(score) + "/" + str(len(questions)) + " correctas")
    print("")
    print("  ¡¡¡ Felicitaciones, Ganaste el premio mayor !!! ")
    print("        !Has obtenido " + str(prize) + " millones de pesos!")
    
run_test()
