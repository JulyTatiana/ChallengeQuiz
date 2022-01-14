from numpy import random
from questions import Preguntas
from models.player import Player
from models.question import Question
import csv

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

    questions = [
        Question(preguntas.nivel1[question1]),
        Question(preguntas.nivel2[question2]),
        Question(preguntas.nivel3[question3]),
        Question(preguntas.nivel4[question4]),
        Question(preguntas.nivel5[question5]),
    ]
    
def greeting():
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
          Nivel 1: 3 millones de pesos
          Nivel 2: 9 millones de pesos
          Nivel 3: 27 millones de pesos
          Nivel 4: 91 millones de pesos
          Nivel 5: 273 millones de pesos
          
          Si desea renunciar en cualquier momento escriba "salir".
          *********************************************************
          """)
    print("")
    player_option = input("Si desea iniciar el juego escriba 1, para ver los anteriores puntajes escriba 2: ")
    return player_option
    
def register_player():

    name = input('Escriba su nombre: ') 
    jugador = Player(name, 0)
        
    return jugador

def assign_player_to_finalscore(player, finalscore):
    
    puntaje = None
    
def get_score():
    record_score = []
    with open('data/score.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            player = Player(row[0], row[1])
            record_score.append(player)
        return record_score

def create_score(name, score):
    recorded_score = get_score()
    with open('data/score.txt', mode='w') as score_file:
        score_writer = csv.writer(score_file, delimiter=',')
        score_writer.writerow([name, score])
        for score in recorded_score:
            score_writer.writerow([score.name, score.finalscore])

def run_test():
    player_option = greeting()

    if player_option == "1":
        jugador = register_player()
    elif player_option == "2":
        historical_score = get_score()
        for score in historical_score:
            print("Nombre: "+ score.name + " obtuvo " + score.finalscore + " puntos.")
        return

    preguntas = Preguntas()
    question1 = random.randint(0,5)
    question2 = random.randint(0,5)
    question3 = random.randint(0,5)
    question4 = random.randint(0,5)
    question5 = random.randint(0,5)

    questions = [
        Question(preguntas.nivel1[question1]),
        Question(preguntas.nivel2[question2]),
        Question(preguntas.nivel3[question3]),
        Question(preguntas.nivel4[question4]),
        Question(preguntas.nivel5[question5]),
    ]
    
    score = 0
    prize = 0
    
    
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
            print( jugador.name + " has ganado " + str(prize) + " millones de pesos!")
            create_score(jugador.name, score)
            return None
        else:
            print(jugador.name + " has perdido, no has ganado ningún premio :C ")
            create_score(jugador.name, score)
            return None
            
    print("Obtuviste " + str(score) + "/" + str(len(questions)) + " correctas")
    print("")
    print("  ¡¡¡ Felicitaciones, " + jugador.name + " .Ganaste el premio mayor !!! ")
    print("        !Has obtenido " + str(prize) + " millones de pesos!")
    create_score(jugador.name, score)
    
run_test()
