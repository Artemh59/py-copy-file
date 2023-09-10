def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if command == "cp":
        with open(old_file, "r") as file_in,\
             open(new_file, "w") as file_out:
            for line in file_in:
                file_out.write(line)
