def copy_file(command: str) -> None:

    if command:
        separete_command = command.split(" ")
        if len(separete_command) > 2 and separete_command[0] == "cp":
            file1 = separete_command[1]
            file2 = separete_command[2]
            if file1 == file2:
                return
            if len(file1) > 0:
                try:
                    with (open(file1, "r") as file_out,
                          open(file2, "w") as file_in):
                        file_in.write(file_out.read())
                except FileNotFoundError:
                    pass
