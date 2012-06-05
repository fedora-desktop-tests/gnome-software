Feature: General actions

  @start_via_menu
  Scenario: Start via command
    * Start Software via menu
    Then Software should start

  @quit_via_shortcut
  Scenario: Ctrl-Q to quit application
    * Start Software via menu
    * Press "<Ctrl>q"
    Then Software shouldn't be running anymore

  @close_via_gnome_panel
  Scenario: Close via menu
    * Start Software via menu
    * Click "Quit" in GApplication menu
    Then Software shouldn't be running anymore
