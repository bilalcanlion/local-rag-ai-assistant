from foundry_local_sdk import Configuration, FoundryLocalManager


def print_model_info(model, index):
    print(f"\n--- Model {index} ---")
    print("Ham gösterim:", model)

    if isinstance(model, dict):
        for key, value in model.items():
            print(f"{key}: {value}")
        return

    important_attrs = [
        "id",
        "model_id",
        "name",
        "alias",
        "task",
        "model_type",
        "provider",
        "version",
        "size",
        "parameters",
        "runtime",
    ]

    for attr in important_attrs:
        if hasattr(model, attr):
            print(f"{attr}: {getattr(model, attr)}")

    if hasattr(model, "__dict__"):
        print("Tüm alanlar:")
        for key, value in model.__dict__.items():
            print(f"{key}: {value}")


def main():
    print("Foundry Local model kataloğu listeleniyor...")

    config = Configuration(app_name="local_rag_ai_assistant")
    FoundryLocalManager.initialize(config)

    manager = FoundryLocalManager.instance
    catalog = manager.catalog

    models = catalog.list_models()

    print("Model liste tipi:", type(models))

    try:
        print("Model sayısı:", len(models))
    except TypeError:
        print("Model sayısı doğrudan okunamadı.")

    for index, model in enumerate(models, start=1):
        print_model_info(model, index)


if __name__ == "__main__":
    main()