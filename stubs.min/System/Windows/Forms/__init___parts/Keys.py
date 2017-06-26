class Keys(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies key codes and modifiers.
    
    enum (flags) Keys, values: A (65), Add (107), Alt (262144), Apps (93), Attn (246), B (66), Back (8), BrowserBack (166), BrowserFavorites (171), BrowserForward (167), BrowserHome (172), BrowserRefresh (168), BrowserSearch (170), BrowserStop (169), C (67), Cancel (3), Capital (20), CapsLock (20), Clear (12), Control (131072), ControlKey (17), Crsel (247), D (68), D0 (48), D1 (49), D2 (50), D3 (51), D4 (52), D5 (53), D6 (54), D7 (55), D8 (56), D9 (57), Decimal (110), Delete (46), Divide (111), Down (40), E (69), End (35), Enter (13), EraseEof (249), Escape (27), Execute (43), Exsel (248), F (70), F1 (112), F10 (121), F11 (122), F12 (123), F13 (124), F14 (125), F15 (126), F16 (127), F17 (128), F18 (129), F19 (130), F2 (113), F20 (131), F21 (132), F22 (133), F23 (134), F24 (135), F3 (114), F4 (115), F5 (116), F6 (117), F7 (118), F8 (119), F9 (120), FinalMode (24), G (71), H (72), HanguelMode (21), HangulMode (21), HanjaMode (25), Help (47), Home (36), I (73), IMEAccept (30), IMEAceept (30), IMEConvert (28), IMEModeChange (31), IMENonconvert (29), Insert (45), J (74), JunjaMode (23), K (75), KanaMode (21), KanjiMode (25), KeyCode (65535), L (76), LaunchApplication1 (182), LaunchApplication2 (183), LaunchMail (180), LButton (1), LControlKey (162), Left (37), LineFeed (10), LMenu (164), LShiftKey (160), LWin (91), M (77), MButton (4), MediaNextTrack (176), MediaPlayPause (179), MediaPreviousTrack (177), MediaStop (178), Menu (18), Modifiers (-65536), Multiply (106), N (78), Next (34), NoName (252), None (0), NumLock (144), NumPad0 (96), NumPad1 (97), NumPad2 (98), NumPad3 (99), NumPad4 (100), NumPad5 (101), NumPad6 (102), NumPad7 (103), NumPad8 (104), NumPad9 (105), O (79), Oem1 (186), Oem102 (226), Oem2 (191), Oem3 (192), Oem4 (219), Oem5 (220), Oem6 (221), Oem7 (222), Oem8 (223), OemBackslash (226), OemClear (254), OemCloseBrackets (221), Oemcomma (188), OemMinus (189), OemOpenBrackets (219), OemPeriod (190), OemPipe (220), Oemplus (187), OemQuestion (191), OemQuotes (222), OemSemicolon (186), Oemtilde (192), P (80), Pa1 (253), Packet (231), PageDown (34), PageUp (33), Pause (19), Play (250), Print (42), PrintScreen (44), Prior (33), ProcessKey (229), Q (81), R (82), RButton (2), RControlKey (163), Return (13), Right (39), RMenu (165), RShiftKey (161), RWin (92), S (83), Scroll (145), Select (41), SelectMedia (181), Separator (108), Shift (65536), ShiftKey (16), Sleep (95), Snapshot (44), Space (32), Subtract (109), T (84), Tab (9), U (85), Up (38), V (86), VolumeDown (174), VolumeMute (173), VolumeUp (175), W (87), X (88), XButton1 (5), XButton2 (6), Y (89), Z (90), Zoom (251)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    A = None
    Add = None
    Alt = None
    Apps = None
    Attn = None
    B = None
    Back = None
    BrowserBack = None
    BrowserFavorites = None
    BrowserForward = None
    BrowserHome = None
    BrowserRefresh = None
    BrowserSearch = None
    BrowserStop = None
    C = None
    Cancel = None
    Capital = None
    CapsLock = None
    Clear = None
    Control = None
    ControlKey = None
    Crsel = None
    D = None
    D0 = None
    D1 = None
    D2 = None
    D3 = None
    D4 = None
    D5 = None
    D6 = None
    D7 = None
    D8 = None
    D9 = None
    Decimal = None
    Delete = None
    Divide = None
    Down = None
    E = None
    End = None
    Enter = None
    EraseEof = None
    Escape = None
    Execute = None
    Exsel = None
    F = None
    F1 = None
    F10 = None
    F11 = None
    F12 = None
    F13 = None
    F14 = None
    F15 = None
    F16 = None
    F17 = None
    F18 = None
    F19 = None
    F2 = None
    F20 = None
    F21 = None
    F22 = None
    F23 = None
    F24 = None
    F3 = None
    F4 = None
    F5 = None
    F6 = None
    F7 = None
    F8 = None
    F9 = None
    FinalMode = None
    G = None
    H = None
    HanguelMode = None
    HangulMode = None
    HanjaMode = None
    Help = None
    Home = None
    I = None
    IMEAccept = None
    IMEAceept = None
    IMEConvert = None
    IMEModeChange = None
    IMENonconvert = None
    Insert = None
    J = None
    JunjaMode = None
    K = None
    KanaMode = None
    KanjiMode = None
    KeyCode = None
    L = None
    LaunchApplication1 = None
    LaunchApplication2 = None
    LaunchMail = None
    LButton = None
    LControlKey = None
    Left = None
    LineFeed = None
    LMenu = None
    LShiftKey = None
    LWin = None
    M = None
    MButton = None
    MediaNextTrack = None
    MediaPlayPause = None
    MediaPreviousTrack = None
    MediaStop = None
    Menu = None
    Modifiers = None
    Multiply = None
    N = None
    Next = None
    NoName = None
    None = None
    NumLock = None
    NumPad0 = None
    NumPad1 = None
    NumPad2 = None
    NumPad3 = None
    NumPad4 = None
    NumPad5 = None
    NumPad6 = None
    NumPad7 = None
    NumPad8 = None
    NumPad9 = None
    O = None
    Oem1 = None
    Oem102 = None
    Oem2 = None
    Oem3 = None
    Oem4 = None
    Oem5 = None
    Oem6 = None
    Oem7 = None
    Oem8 = None
    OemBackslash = None
    OemClear = None
    OemCloseBrackets = None
    Oemcomma = None
    OemMinus = None
    OemOpenBrackets = None
    OemPeriod = None
    OemPipe = None
    Oemplus = None
    OemQuestion = None
    OemQuotes = None
    OemSemicolon = None
    Oemtilde = None
    P = None
    Pa1 = None
    Packet = None
    PageDown = None
    PageUp = None
    Pause = None
    Play = None
    Print = None
    PrintScreen = None
    Prior = None
    ProcessKey = None
    Q = None
    R = None
    RButton = None
    RControlKey = None
    Return = None
    Right = None
    RMenu = None
    RShiftKey = None
    RWin = None
    S = None
    Scroll = None
    Select = None
    SelectMedia = None
    Separator = None
    Shift = None
    ShiftKey = None
    Sleep = None
    Snapshot = None
    Space = None
    Subtract = None
    T = None
    Tab = None
    U = None
    Up = None
    V = None
    value__ = None
    VolumeDown = None
    VolumeMute = None
    VolumeUp = None
    W = None
    X = None
    XButton1 = None
    XButton2 = None
    Y = None
    Z = None
    Zoom = None
