Help on package curses:

NNAAMMEE
    curses - curses

MMOODDUULLEE  RREEFFEERREENNCCEE
    https://docs.python.org/3.12/library/curses.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DDEESSCCRRIIPPTTIIOONN
    The main package for curses support for Python.  Normally used by importing
    the package, and perhaps a particular module inside it.

       import curses
       from curses import textpad
       curses.initscr()
       ...

PPAACCKKAAGGEE  CCOONNTTEENNTTSS
    ascii
    has_key
    panel
    textpad

FFUUNNCCTTIIOONNSS
    bbaauuddrraattee()
        Return the output speed of the terminal in bits per second.

    bbeeeepp()
        Emit a short attention sound.

    ccaann__cchhaannggee__ccoolloorr()
        Return True if the programmer can change the colors displayed by the terminal.

    ccbbrreeaakk(flag=True, /)
        Enter cbreak mode.

          flag
            If false, the effect is the same as calling nocbreak().

        In cbreak mode (sometimes called "rare" mode) normal tty line buffering is
        turned off and characters are available to be read one by one.  However,
        unlike raw mode, special characters (interrupt, quit, suspend, and flow
        control) retain their effects on the tty driver and calling program.
        Calling first raw() then cbreak() leaves the terminal in cbreak mode.

    ccoolloorr__ccoonntteenntt(color_number, /)
        Return the red, green, and blue (RGB) components of the specified color.

          color_number
            The number of the color (0 - (COLORS-1)).

        A 3-tuple is returned, containing the R, G, B values for the given color,
        which will be between 0 (no component) and 1000 (maximum amount of component).

    ccoolloorr__ppaaiirr(pair_number, /)
        Return the attribute value for displaying text in the specified color.

          pair_number
            The number of the color pair.

        This attribute value can be combined with A_STANDOUT, A_REVERSE, and the
        other A_* attributes.  pair_number() is the counterpart to this function.

    ccuurrss__sseett(visibility, /)
        Set the cursor state.

          visibility
            0 for invisible, 1 for normal visible, or 2 for very visible.

        If the terminal supports the visibility requested, the previous cursor
        state is returned; otherwise, an exception is raised.  On many terminals,
        the "visible" mode is an underline cursor and the "very visible" mode is
        a block cursor.

    ddeeff__pprroogg__mmooddee()
        Save the current terminal mode as the "program" mode.

        The "program" mode is the mode when the running program is using curses.

        Subsequent calls to reset_prog_mode() will restore this mode.

    ddeeff__sshheellll__mmooddee()
        Save the current terminal mode as the "shell" mode.

        The "shell" mode is the mode when the running program is not using curses.

        Subsequent calls to reset_shell_mode() will restore this mode.

    ddeellaayy__oouuttppuutt(ms, /)
        Insert a pause in output.

        ms
          Duration in milliseconds.

    ddoouuppddaattee()
        Update the physical screen to match the virtual screen.

    eecchhoo(flag=True, /)
        Enter echo mode.

          flag
            If false, the effect is the same as calling noecho().

        In echo mode, each character input is echoed to the screen as it is entered.

    eennddwwiinn()
        De-initialize the library, and return terminal to normal status.

    eerraasseecchhaarr()
        Return the user's current erase character.

    ffiilltteerr()

    ffllaasshh()
        Flash the screen.

        That is, change it to reverse-video and then change it back in a short interval.

    fflluusshhiinnpp()
        Flush all input buffers.

        This throws away any typeahead that has been typed by the user and has not
        yet been processed by the program.

    ggeett__eessccddeellaayy()
        Gets the curses ESCDELAY setting.

        Gets the number of milliseconds to wait after reading an escape character,
        to distinguish between an individual escape character entered on the
        keyboard from escape sequences sent by cursor and function keys.

    ggeett__ttaabbssiizzee()
        Gets the curses TABSIZE setting.

        Gets the number of columns used by the curses library when converting a tab
        character to spaces as it adds the tab to a window.

    ggeettmmoouussee()
        Retrieve the queued mouse event.

        After getch() returns KEY_MOUSE to signal a mouse event, this function
        returns a 5-tuple (id, x, y, z, bstate).

    ggeettssyyxx()
        Return the current coordinates of the virtual screen cursor.

        Return a (y, x) tuple.  If leaveok is currently true, return (-1, -1).

    ggeettwwiinn(file, /)
        Read window related data stored in the file by an earlier putwin() call.

        The routine then creates and initializes a new window using that data,
        returning the new window object.

    hhaallffddeellaayy(tenths, /)
        Enter half-delay mode.

          tenths
            Maximal blocking delay in tenths of seconds (1 - 255).

        Use nocbreak() to leave half-delay mode.

    hhaass__ccoolloorrss()
        Return True if the terminal can display colors; otherwise, return False.

    hhaass__eexxtteennddeedd__ccoolloorr__ssuuppppoorrtt()
        Return True if the module supports extended colors; otherwise, return False.

        Extended color support allows more than 256 color-pairs for terminals
        that support more than 16 colors (e.g. xterm-256color).

    hhaass__iicc()
        Return True if the terminal has insert- and delete-character capabilities.

    hhaass__iill()
        Return True if the terminal has insert- and delete-line capabilities.

    hhaass__kkeeyy(key, /)
        Return True if the current terminal type recognizes a key with that value.

        key
          Key number.

    iinniitt__ccoolloorr(color_number, r, g, b, /)
        Change the definition of a color.

          color_number
            The number of the color to be changed (0 - (COLORS-1)).
          r
            Red component (0 - 1000).
          g
            Green component (0 - 1000).
          b
            Blue component (0 - 1000).

        When init_color() is used, all occurrences of that color on the screen
        immediately change to the new definition.  This function is a no-op on
        most terminals; it is active only if can_change_color() returns true.

    iinniitt__ppaaiirr(pair_number, fg, bg, /)
        Change the definition of a color-pair.

          pair_number
            The number of the color-pair to be changed (1 - (COLOR_PAIRS-1)).
          fg
            Foreground color number (-1 - (COLORS-1)).
          bg
            Background color number (-1 - (COLORS-1)).

        If the color-pair was previously initialized, the screen is refreshed and
        all occurrences of that color-pair are changed to the new definition.

    iinniittssccrr()

    iinnttrrfflluusshh(flag, /)

    iiss__tteerrmm__rreessiizzeedd(nlines, ncols, /)
        Return True if resize_term() would modify the window structure, False otherwise.

        nlines
          Height.
        ncols
          Width.

    iisseennddwwiinn()
        Return True if endwin() has been called.

    kkeeyynnaammee(key, /)
        Return the name of specified key.

        key
          Key number.

    kkiillllcchhaarr()
        Return the user's current line kill character.

    lloonnggnnaammee()
        Return the terminfo long name field describing the current terminal.

        The maximum length of a verbose description is 128 characters.  It is defined
        only after the call to initscr().

    mmeettaa(yes, /)
        Enable/disable meta keys.

        If yes is True, allow 8-bit characters to be input.  If yes is False,
        allow only 7-bit characters.

    mmoouusseeiinntteerrvvaall(interval, /)
        Set and retrieve the maximum time between press and release in a click.

          interval
            Time in milliseconds.

        Set the maximum time that can elapse between press and release events in
        order for them to be recognized as a click, and return the previous interval
        value.

    mmoouusseemmaasskk(newmask, /)
        Set the mouse events to be reported, and return a tuple (availmask, oldmask).

        Return a tuple (availmask, oldmask).  availmask indicates which of the
        specified mouse events can be reported; on complete failure it returns 0.
        oldmask is the previous value of the given window's mouse event mask.
        If this function is never called, no mouse events are ever reported.

    nnaappmmss(ms, /)
        Sleep for specified time.

        ms
          Duration in milliseconds.

    nneewwppaadd(nlines, ncols, /)
        Create and return a pointer to a new pad data structure.

        nlines
          Height.
        ncols
          Width.

    nneewwwwiinn(...)
        newwin(nlines, ncols, [begin_y=0, begin_x=0])
        Return a new window.

          nlines
            Height.
          ncols
            Width.
          begin_y
            Top side y-coordinate.
          begin_x
            Left side x-coordinate.

        By default, the window will extend from the specified position to the lower
        right corner of the screen.

    nnll(flag=True, /)
        Enter newline mode.

          flag
            If false, the effect is the same as calling nonl().

        This mode translates the return key into newline on input, and translates
        newline into return and line-feed on output.  Newline mode is initially on.

    nnooccbbrreeaakk()
        Leave cbreak mode.

        Return to normal "cooked" mode with line buffering.

    nnooeecchhoo()
        Leave echo mode.

        Echoing of input characters is turned off.

    nnoonnll()
        Leave newline mode.

        Disable translation of return into newline on input, and disable low-level
        translation of newline into newline/return on output.

    nnooqqiifflluusshh()
        Disable queue flushing.

        When queue flushing is disabled, normal flush of input and output queues
        associated with the INTR, QUIT and SUSP characters will not be done.

    nnoorraaww()
        Leave raw mode.

        Return to normal "cooked" mode with line buffering.

    ppaaiirr__ccoonntteenntt(pair_number, /)
        Return a tuple (fg, bg) containing the colors for the requested color pair.

        pair_number
          The number of the color pair (0 - (COLOR_PAIRS-1)).

    ppaaiirr__nnuummbbeerr(attr, /)
        Return the number of the color-pair set by the specified attribute value.

        color_pair() is the counterpart to this function.

    ppuuttpp(string, /)
        Emit the value of a specified terminfo capability for the current terminal.

        Note that the output of putp() always goes to standard output.

    qqiifflluusshh(flag=True, /)
        Enable queue flushing.

          flag
            If false, the effect is the same as calling noqiflush().

        If queue flushing is enabled, all output in the display driver queue
        will be flushed when the INTR, QUIT and SUSP characters are read.

    rraaww(flag=True, /)
        Enter raw mode.

          flag
            If false, the effect is the same as calling noraw().

        In raw mode, normal line buffering and processing of interrupt, quit,
        suspend, and flow control keys are turned off; characters are presented to
        curses input functions one by one.

    rreesseett__pprroogg__mmooddee()
        Restore the terminal to "program" mode, as previously saved by def_prog_mode().

    rreesseett__sshheellll__mmooddee()
        Restore the terminal to "shell" mode, as previously saved by def_shell_mode().

    rreesseettttyy()
        Restore terminal mode.

    rreessiizzee__tteerrmm(nlines, ncols, /)
        Backend function used by resizeterm(), performing most of the work.

          nlines
            Height.
          ncols
            Width.

        When resizing the windows, resize_term() blank-fills the areas that are
        extended.  The calling application should fill in these areas with appropriate
        data.  The resize_term() function attempts to resize all windows.  However,
        due to the calling convention of pads, it is not possible to resize these
        without additional interaction with the application.

    rreessiizzeetteerrmm(nlines, ncols, /)
        Resize the standard and current windows to the specified dimensions.

          nlines
            Height.
          ncols
            Width.

        Adjusts other bookkeeping data used by the curses library that record the
        window dimensions (in particular the SIGWINCH handler).

    ssaavveettttyy()
        Save terminal mode.

    sseett__eessccddeellaayy(ms, /)
        Sets the curses ESCDELAY setting.

          ms
            length of the delay in milliseconds.

        Sets the number of milliseconds to wait after reading an escape character,
        to distinguish between an individual escape character entered on the
        keyboard from escape sequences sent by cursor and function keys.

    sseett__ttaabbssiizzee(size, /)
        Sets the curses TABSIZE setting.

          size
            rendered cell width of a tab character.

        Sets the number of columns used by the curses library when converting a tab
        character to spaces as it adds the tab to a window.

    sseettssyyxx(y, x, /)
        Set the virtual screen cursor.

          y
            Y-coordinate.
          x
            X-coordinate.

        If y and x are both -1, then leaveok is set.

    sseettuupptteerrmm(term=None, fd=-1)
        Initialize the terminal.

        term
          Terminal name.
          If omitted, the value of the TERM environment variable will be used.
        fd
          File descriptor to which any initialization sequences will be sent.
          If not supplied, the file descriptor for sys.stdout will be used.

    ssttaarrtt__ccoolloorr()

    tteerrmmaattttrrss()
        Return a logical OR of all video attributes supported by the terminal.

    tteerrmmnnaammee()
        Return the value of the environment variable TERM, truncated to 14 characters.

    ttiiggeettffllaagg(capname, /)
        Return the value of the Boolean capability.

          capname
            The terminfo capability name.

        The value -1 is returned if capname is not a Boolean capability, or 0 if
        it is canceled or absent from the terminal description.

    ttiiggeettnnuumm(capname, /)
        Return the value of the numeric capability.

          capname
            The terminfo capability name.

        The value -2 is returned if capname is not a numeric capability, or -1 if
        it is canceled or absent from the terminal description.

    ttiiggeettssttrr(capname, /)
        Return the value of the string capability.

          capname
            The terminfo capability name.

        None is returned if capname is not a string capability, or is canceled or
        absent from the terminal description.

    ttppaarrmm(str, i1=0, i2=0, i3=0, i4=0, i5=0, i6=0, i7=0, i8=0, i9=0, /)
        Instantiate the specified byte string with the supplied parameters.

        str
          Parameterized byte string obtained from the terminfo database.

    ttyyppeeaahheeaadd(fd, /)
        Specify that the file descriptor fd be used for typeahead checking.

          fd
            File descriptor.

        If fd is -1, then no typeahead checking is done.

    uunnccttrrll(ch, /)
        Return a string which is a printable representation of the character ch.

        Control characters are displayed as a caret followed by the character,
        for example as ^C.  Printing characters are left as they are.

    uunnggeett__wwcchh(ch, /)
        Push ch so the next get_wch() will return it.

    uunnggeettcchh(ch, /)
        Push ch so the next getch() will return it.

    uunnggeettmmoouussee(id, x, y, z, bstate, /)
        Push a KEY_MOUSE event onto the input queue.

        The following getmouse() will return the given state data.

    uuppddaattee__lliinneess__ccoollss()

    uussee__ddeeffaauulltt__ccoolloorrss()
        Allow use of default values for colors on terminals supporting this feature.

        Use this to support transparency in your application.  The default color
        is assigned to the color number -1.

    uussee__eennvv(flag, /)
        Use environment variables LINES and COLUMNS.

        If used, this function should be called before initscr() or newterm() are
        called.

        When flag is False, the values of lines and columns specified in the terminfo
        database will be used, even if environment variables LINES and COLUMNS (used
        by default) are set, or if curses is running in a window (in which case
        default behavior would be to use the window size if LINES and COLUMNS are
        not set).

    wwrraappppeerr(func, /, *args, **kwds)
        Wrapper function that initializes curses and calls another function,
        restoring normal keyboard/screen behavior on error.
        The callable object 'func' is then passed the main window 'stdscr'
        as its first argument, followed by any other arguments passed to
        wrapper().

DDAATTAA
    AALLLL__MMOOUUSSEE__EEVVEENNTTSS = 268435455
    AA__AALLTTCCHHAARRSSEETT = 4194304
    AA__AATTTTRRIIBBUUTTEESS = 4294967040
    AA__BBLLIINNKK = 524288
    AA__BBOOLLDD = 2097152
    AA__CCHHAARRTTEEXXTT = 255
    AA__CCOOLLOORR = 65280
    AA__DDIIMM = 1048576
    AA__HHOORRIIZZOONNTTAALL = 33554432
    AA__IINNVVIISS = 8388608
    AA__IITTAALLIICC = 2147483648
    AA__LLEEFFTT = 67108864
    AA__LLOOWW = 134217728
    AA__NNOORRMMAALL = 0
    AA__PPRROOTTEECCTT = 16777216
    AA__RREEVVEERRSSEE = 262144
    AA__RRIIGGHHTT = 268435456
    AA__SSTTAANNDDOOUUTT = 65536
    AA__TTOOPP = 536870912
    AA__UUNNDDEERRLLIINNEE = 131072
    AA__VVEERRTTIICCAALL = 1073741824
    BBUUTTTTOONN11__CCLLIICCKKEEDD = 4
    BBUUTTTTOONN11__DDOOUUBBLLEE__CCLLIICCKKEEDD = 8
    BBUUTTTTOONN11__PPRREESSSSEEDD = 2
    BBUUTTTTOONN11__RREELLEEAASSEEDD = 1
    BBUUTTTTOONN11__TTRRIIPPLLEE__CCLLIICCKKEEDD = 16
    BBUUTTTTOONN22__CCLLIICCKKEEDD = 128
    BBUUTTTTOONN22__DDOOUUBBLLEE__CCLLIICCKKEEDD = 256
    BBUUTTTTOONN22__PPRREESSSSEEDD = 64
    BBUUTTTTOONN22__RREELLEEAASSEEDD = 32
    BBUUTTTTOONN22__TTRRIIPPLLEE__CCLLIICCKKEEDD = 512
    BBUUTTTTOONN33__CCLLIICCKKEEDD = 4096
    BBUUTTTTOONN33__DDOOUUBBLLEE__CCLLIICCKKEEDD = 8192
    BBUUTTTTOONN33__PPRREESSSSEEDD = 2048
    BBUUTTTTOONN33__RREELLEEAASSEEDD = 1024
    BBUUTTTTOONN33__TTRRIIPPLLEE__CCLLIICCKKEEDD = 16384
    BBUUTTTTOONN44__CCLLIICCKKEEDD = 131072
    BBUUTTTTOONN44__DDOOUUBBLLEE__CCLLIICCKKEEDD = 262144
    BBUUTTTTOONN44__PPRREESSSSEEDD = 65536
    BBUUTTTTOONN44__RREELLEEAASSEEDD = 32768
    BBUUTTTTOONN44__TTRRIIPPLLEE__CCLLIICCKKEEDD = 524288
    BBUUTTTTOONN55__CCLLIICCKKEEDD = 4194304
    BBUUTTTTOONN55__DDOOUUBBLLEE__CCLLIICCKKEEDD = 8388608
    BBUUTTTTOONN55__PPRREESSSSEEDD = 2097152
    BBUUTTTTOONN55__RREELLEEAASSEEDD = 1048576
    BBUUTTTTOONN55__TTRRIIPPLLEE__CCLLIICCKKEEDD = 16777216
    BBUUTTTTOONN__AALLTT = 134217728
    BBUUTTTTOONN__CCTTRRLL = 33554432
    BBUUTTTTOONN__SSHHIIFFTT = 67108864
    CCOOLLOORR__BBLLAACCKK = 0
    CCOOLLOORR__BBLLUUEE = 4
    CCOOLLOORR__CCYYAANN = 6
    CCOOLLOORR__GGRREEEENN = 2
    CCOOLLOORR__MMAAGGEENNTTAA = 5
    CCOOLLOORR__RREEDD = 1
    CCOOLLOORR__WWHHIITTEE = 7
    CCOOLLOORR__YYEELLLLOOWW = 3
    EERRRR = -1
    KKEEYY__AA11 = 348
    KKEEYY__AA33 = 349
    KKEEYY__BB22 = 350
    KKEEYY__BBAACCKKSSPPAACCEE = 263
    KKEEYY__BBEEGG = 354
    KKEEYY__BBRREEAAKK = 257
    KKEEYY__BBTTAABB = 353
    KKEEYY__CC11 = 351
    KKEEYY__CC33 = 352
    KKEEYY__CCAANNCCEELL = 355
    KKEEYY__CCAATTAABB = 342
    KKEEYY__CCLLEEAARR = 333
    KKEEYY__CCLLOOSSEE = 356
    KKEEYY__CCOOMMMMAANNDD = 357
    KKEEYY__CCOOPPYY = 358
    KKEEYY__CCRREEAATTEE = 359
    KKEEYY__CCTTAABB = 341
    KKEEYY__DDCC = 330
    KKEEYY__DDLL = 328
    KKEEYY__DDOOWWNN = 258
    KKEEYY__EEIICC = 332
    KKEEYY__EENNDD = 360
    KKEEYY__EENNTTEERR = 343
    KKEEYY__EEOOLL = 335
    KKEEYY__EEOOSS = 334
    KKEEYY__EEXXIITT = 361
    KKEEYY__FF00 = 264
    KKEEYY__FF11 = 265
    KKEEYY__FF1100 = 274
    KKEEYY__FF1111 = 275
    KKEEYY__FF1122 = 276
    KKEEYY__FF1133 = 277
    KKEEYY__FF1144 = 278
    KKEEYY__FF1155 = 279
    KKEEYY__FF1166 = 280
    KKEEYY__FF1177 = 281
    KKEEYY__FF1188 = 282
    KKEEYY__FF1199 = 283
    KKEEYY__FF22 = 266
    KKEEYY__FF2200 = 284
    KKEEYY__FF2211 = 285
    KKEEYY__FF2222 = 286
    KKEEYY__FF2233 = 287
    KKEEYY__FF2244 = 288
    KKEEYY__FF2255 = 289
    KKEEYY__FF2266 = 290
    KKEEYY__FF2277 = 291
    KKEEYY__FF2288 = 292
    KKEEYY__FF2299 = 293
    KKEEYY__FF33 = 267
    KKEEYY__FF3300 = 294
    KKEEYY__FF3311 = 295
    KKEEYY__FF3322 = 296
    KKEEYY__FF3333 = 297
    KKEEYY__FF3344 = 298
    KKEEYY__FF3355 = 299
    KKEEYY__FF3366 = 300
    KKEEYY__FF3377 = 301
    KKEEYY__FF3388 = 302
    KKEEYY__FF3399 = 303
    KKEEYY__FF44 = 268
    KKEEYY__FF4400 = 304
    KKEEYY__FF4411 = 305
    KKEEYY__FF4422 = 306
    KKEEYY__FF4433 = 307
    KKEEYY__FF4444 = 308
    KKEEYY__FF4455 = 309
    KKEEYY__FF4466 = 310
    KKEEYY__FF4477 = 311
    KKEEYY__FF4488 = 312
    KKEEYY__FF4499 = 313
    KKEEYY__FF55 = 269
    KKEEYY__FF5500 = 314
    KKEEYY__FF5511 = 315
    KKEEYY__FF5522 = 316
    KKEEYY__FF5533 = 317
    KKEEYY__FF5544 = 318
    KKEEYY__FF5555 = 319
    KKEEYY__FF5566 = 320
    KKEEYY__FF5577 = 321
    KKEEYY__FF5588 = 322
    KKEEYY__FF5599 = 323
    KKEEYY__FF66 = 270
    KKEEYY__FF6600 = 324
    KKEEYY__FF6611 = 325
    KKEEYY__FF6622 = 326
    KKEEYY__FF6633 = 327
    KKEEYY__FF77 = 271
    KKEEYY__FF88 = 272
    KKEEYY__FF99 = 273
    KKEEYY__FFIINNDD = 362
    KKEEYY__HHEELLPP = 363
    KKEEYY__HHOOMMEE = 262
    KKEEYY__IICC = 331
    KKEEYY__IILL = 329
    KKEEYY__LLEEFFTT = 260
    KKEEYY__LLLL = 347
    KKEEYY__MMAARRKK = 364
    KKEEYY__MMAAXX = 511
    KKEEYY__MMEESSSSAAGGEE = 365
    KKEEYY__MMIINN = 257
    KKEEYY__MMOOUUSSEE = 409
    KKEEYY__MMOOVVEE = 366
    KKEEYY__NNEEXXTT = 367
    KKEEYY__NNPPAAGGEE = 338
    KKEEYY__OOPPEENN = 368
    KKEEYY__OOPPTTIIOONNSS = 369
    KKEEYY__PPPPAAGGEE = 339
    KKEEYY__PPRREEVVIIOOUUSS = 370
    KKEEYY__PPRRIINNTT = 346
    KKEEYY__RREEDDOO = 371
    KKEEYY__RREEFFEERREENNCCEE = 372
    KKEEYY__RREEFFRREESSHH = 373
    KKEEYY__RREEPPLLAACCEE = 374
    KKEEYY__RREESSEETT = 345
    KKEEYY__RREESSIIZZEE = 410
    KKEEYY__RREESSTTAARRTT = 375
    KKEEYY__RREESSUUMMEE = 376
    KKEEYY__RRIIGGHHTT = 261
    KKEEYY__SSAAVVEE = 377
    KKEEYY__SSBBEEGG = 378
    KKEEYY__SSCCAANNCCEELL = 379
    KKEEYY__SSCCOOMMMMAANNDD = 380
    KKEEYY__SSCCOOPPYY = 381
    KKEEYY__SSCCRREEAATTEE = 382
    KKEEYY__SSDDCC = 383
    KKEEYY__SSDDLL = 384
    KKEEYY__SSEELLEECCTT = 385
    KKEEYY__SSEENNDD = 386
    KKEEYY__SSEEOOLL = 387
    KKEEYY__SSEEXXIITT = 388
    KKEEYY__SSFF = 336
    KKEEYY__SSFFIINNDD = 389
    KKEEYY__SSHHEELLPP = 390
    KKEEYY__SSHHOOMMEE = 391
    KKEEYY__SSIICC = 392
    KKEEYY__SSLLEEFFTT = 393
    KKEEYY__SSMMEESSSSAAGGEE = 394
    KKEEYY__SSMMOOVVEE = 395
    KKEEYY__SSNNEEXXTT = 396
    KKEEYY__SSOOPPTTIIOONNSS = 397
    KKEEYY__SSPPRREEVVIIOOUUSS = 398
    KKEEYY__SSPPRRIINNTT = 399
    KKEEYY__SSRR = 337
    KKEEYY__SSRREEDDOO = 400
    KKEEYY__SSRREEPPLLAACCEE = 401
    KKEEYY__SSRREESSEETT = 344
    KKEEYY__SSRRIIGGHHTT = 402
    KKEEYY__SSRRSSUUMMEE = 403
    KKEEYY__SSSSAAVVEE = 404
    KKEEYY__SSSSUUSSPPEENNDD = 405
    KKEEYY__SSTTAABB = 340
    KKEEYY__SSUUNNDDOO = 406
    KKEEYY__SSUUSSPPEENNDD = 407
    KKEEYY__UUNNDDOO = 408
    KKEEYY__UUPP = 259
    OOKK = 0
    RREEPPOORRTT__MMOOUUSSEE__PPOOSSIITTIIOONN = 268435456
    nnccuurrsseess__vveerrssiioonn = curses.ncurses_version(major=6, minor=4, patch=20240...
    vveerrssiioonn = b'2.2'

FFIILLEE
    /usr/lib/python3.12/curses/__init__.py

