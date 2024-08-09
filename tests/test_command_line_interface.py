from eggsample.command_line_interface import main
from eggsample.eggsellent_cook import condiments_tray

def test_main(capsys):
    """Test the main function."""
    main()
    captured = capsys.readouterr()
    assert "Your food." in captured.out
    assert ", ".join(condiments_tray) in captured.out
