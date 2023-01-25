while True:
    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        # Event handling for range of differnt key presses
        if event.type == pygame.KEYDOWN:
            pass