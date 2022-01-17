from events.event_args import EventArgs

class CoffeeRecipeDoneEventArgs(EventArgs):
    # args: (Coffee)
    pass

class MainEventArgs(EventArgs):
    EVENT_CODE_NEW_COFFEE       = 0b00000001

class PreparedDoneArgs(EventArgs):
    pass

class RefreshMilkArgs(EventArgs):
    pass

class WaitPosArgs(EventArgs):
    pass

class MailingArgs(EventArgs):
    pass
