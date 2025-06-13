from handlers import DatasetHandler, ModelHandler
import os

# ----- global vars -----

# useful stuff
dataset_handler = None
model_handler = None

# stats
correct_predictions_user = 0
correct_predictions_model = 0
total_predictions = 0


# ----- functions -----
def setup(dataset_handler_instance: DatasetHandler, model_handler_instance: ModelHandler):
    global dataset_handler, model_handler

    dataset_handler = dataset_handler_instance
    model_handler = model_handler_instance

def clear_on_input():
    input("Press ENTER to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_stats():
    global correct_predictions_model, correct_predictions_user, total_predictions
    clear()
    if total_predictions == 0:
        print("No stats to display.")
        clear_on_input()
        return
    
    print("-- [PREDICTION STATS] --\n")
    print("\tACCURACY\tTIMES CORRECT")
    print(f"USER\t", str(1/total_predictions*correct_predictions_user)[:4], "\t\t", str(correct_predictions_user))
    print(f"MODEL\t", str(1/total_predictions*correct_predictions_model)[:4], "\t\t", str(correct_predictions_model))
    print()
    print("TOTAL GAMES:\t", str(total_predictions))
    clear_on_input()

def get_user_prediction():
    while True:
        prediction = input("Is it sarcasm? [0/1]: ")

        if prediction in ["0", "1"]:
            return int(prediction)
        
        print("Invalid Input.\n")

def game_loop():
    global correct_predictions_model, correct_predictions_user, total_predictions

    while True:
        clear()
        total_predictions += 1
        is_sarcastic, headline = dataset_handler.get_random_entry()

        print("-- [Human VS Machine: Sarcasm Edition] --\n")
        print("HEADLINE:\n\t", headline)
        prediction_user = get_user_prediction()
        prediction_model = model_handler.predict(headline)

        print() # newline

        print(f"SARCASM: {is_sarcastic}")
        # user
        if prediction_user == is_sarcastic:
            print(f"User: {prediction_user}\t\tcorrect")
            correct_predictions_user += 1
        else:
            print(f"User: {prediction_user}\t\tincorrect")

        # model
        if prediction_model == is_sarcastic:
            print(f"Model: {prediction_model}\tcorrect")
            correct_predictions_model += 1
        else:
            print(f"Model: {prediction_model}\tincorrect")
        
        user_input = input("\nPress ENTER to play again, cancel with 'n': ")
        if user_input.lower() == "n":
            break

def predict():
    clear()
    print("-- [MODEL PREDICTION] --\n")
    print("Enter the headline to predict:")
    headline = input()
    model_prediction = model_handler.predict(headline)
    print("\nModel prediction: ", "Is sarcastic (1)" if model_prediction == 1 else "Is not sarcastic (0)")
    clear_on_input()

def menu_loop():
    while True:
        clear()
        print("-- [SARCASM MODEL] --")
        print("1) predict headline")
        print("2) play against model")
        print("3) user/model game stats")
        print("4) exit")
        print("Select option:")

        user_input = input()
        match user_input:
            case "1":
                predict()
            case "2":
                game_loop()
            case "3":
                print_stats()
            case "4":
                print("Goodbye!")
                return
            case _:
                print("Invalid Input")

