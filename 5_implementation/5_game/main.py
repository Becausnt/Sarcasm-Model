import handlers

# ----- Global Vars -----
model_handler = None
dataset_handler = None

# ----- Functions -----

def setup():
    global model_handler, dataset_handler

    model_handler = handlers.ModelHandler()
    dataset_handler = handlers.DatasetHandler()

# UI in Console
def launch_cli():
    import cli
    cli.setup(dataset_handler, model_handler)
    cli.menu_loop()

# ----- Entrypoint -----
if __name__ == "__main__":
    print("Loading...")
    setup()
    launch_cli()
    exit(1)