## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - action_buscar_diahora
  - action_ask_agenda
* escolher_dia_hora
  - action_salva_escolha

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
