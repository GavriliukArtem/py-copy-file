def copy_file(command: str) -> None:

    if command:
        separate_command = command.split(" ")
        if len(separate_command) == 3 and separate_command[0] == "cp":
            source_file = separate_command[1]
            destination_file = separate_command[2]
            if source_file == destination_file:
                return
            if len(source_file) > 0:
                try:
                    with (open(source_file, "r") as source_file,
                          open(destination_file, "w") as destination_file):
                        destination_file .write(source_file .read())
                except FileNotFoundError:
                    pass
