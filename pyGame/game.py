import pygame
import game_modules.deadline_22_02_dialogue_module as dialogue_module
import game_modules.deadline_22_02_menu as menu
import game_modules.deadline_22_02_mini as mini
import game_modules.deadline_22_02_generate_nums as generate_nums

win_size = (800, 600)
win = pygame.display.set_mode((win_size))


mainWin = menu.mainWindow()
aftetrMenu = mainWin.showMenu()
if aftetrMenu:
    win.fill((0, 0, 0))
    dial1 = dialogue_module.DialogueWindow(win)
    dial1.runDialogue1()

    main_el = mini.minigame(win, generate_nums.lucky(16), [i for i in range(1, 17)], 10, 'Lucky')
    result = main_el.run_game()

    win.fill((0, 0, 0))
    dial2 = dialogue_module.DialogueWindow(win)
    dial2.runDialogue2()

    win.fill((0, 0, 0))
    dial3 = dialogue_module.DialogueWindow(win)
    dial3.runDialogue3()

    result = False
    while result != 'win' and result != 'quit':
        main_el = mini.minigame(win, generate_nums.even(16), [i for i in range(1, 17)], 9999, 'Even')
        result = main_el.run_game()

    win.fill((0, 0, 0))
    dial4 = dialogue_module.DialogueWindow(win)
    dial4.runDialogue4()

    result = False
    while result != 'win' and result != 'quit':
        main_el = mini.minigame(win, generate_nums.lucky(16), [i for i in range(1, 17)], 9999, 'Lucky')
        result = main_el.run_game()

    win.fill((0, 0, 0))
    dial5 = dialogue_module.DialogueWindow(win)
    dial5.runDialogue5()

    result = False
    while result != 'win' and result != 'quit':
        main_el = mini.minigame(win, generate_nums.ulam(16), [i for i in range(1, 17)], 9999, "Ulam's")
        result = main_el.run_game()


    win.fill((0, 0, 0))
    dial6 = dialogue_module.DialogueWindow(win)
    dial6.runDialogue6()

    result = False
    while result != 'win' and result != 'quit':
        main_el = mini.minigame(win, generate_nums.even(16), [i for i in range(1, 17)], 40, 'Even')
        result = main_el.run_game()
    result = False
    while result != 'win' and result != 'quit':
        main_el = mini.minigame(win, generate_nums.lucky(16), [i for i in range(1, 17)], 40, 'Lucky')
        result = main_el.run_game()
    result = False
    while result != 'win' and result != 'quit':
        main_el = mini.minigame(win, generate_nums.ulam(16), [i for i in range(1, 17)], 40, "Ulam's")
        result = main_el.run_game()

    win.fill((0, 0, 0))
    dial7 = dialogue_module.DialogueWindow(win)
    dial7.runDialogue7()

else:
    pygame.quit()
