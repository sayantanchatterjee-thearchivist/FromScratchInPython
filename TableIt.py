BoxDrawing = {
    "light": {
        "solid": {
            "vertical":    "│",
            "horizontal":  "─",
            "top-left":    "┌",
            "top-right":   "┐",
            "bottom-left": "└",
            "bottom-right":"┘",
            "cross":       "┼",
            "tee-up":      "┴",
            "tee-down":    "┬",
            "tee-right":   "├",
            "tee-left":    "┤"
        },
        "dashed": {
            "vertical":    "┆",
            "horizontal":  "┄",
            "top-left":    "┌",
            "top-right":   "┐",
            "bottom-left": "└",
            "bottom-right":"┘",
            "cross":       "┼",
            "tee-up":      "┴",
            "tee-down":    "┬",
            "tee-right":   "├",
            "tee-left":    "┤"
        },
        "double-dashed": {
            "vertical":    "╎",
            "horizontal":  "╌",
            "top-left":    "┌",
            "top-right":   "┐",
            "bottom-left": "└",
            "bottom-right":"┘",
            "cross":       "┼",
            "tee-up":      "┴",
            "tee-down":    "┬",
            "tee-right":   "├",
            "tee-left":    "┤"
        },
        "quadruple-dashed": {
            "vertical":    "┊",
            "horizontal":  "┈",
            "top-left":    "┌",
            "top-right":   "┐",
            "bottom-left": "└",
            "bottom-right":"┘",
            "cross":       "┼",
            "tee-up":      "┴",
            "tee-down":    "┬",
            "tee-right":   "├",
            "tee-left":    "┤"
        },
        "curved": {
            "vertical":    "│",
            "horizontal":  "─",
            "top-left":    "╭",
            "top-right":   "╮",
            "bottom-left": "╰",
            "bottom-right":"╯",
            "cross":       "┼",
            "tee-up":      "┴",
            "tee-down":    "┬",
            "tee-right":   "├",
            "tee-left":    "┤"
        }
    },
    "heavy": {
        "solid": {
            "vertical":    "┃",
            "horizontal":  "━",
            "top-left":    "┏",
            "top-right":   "┓",
            "bottom-left": "┗",
            "bottom-right":"┛",
            "cross":       "╋",
            "tee-up":      "┻",
            "tee-down":    "┳",
            "tee-right":   "┣",
            "tee-left":    "┫"
        },
        "dashed": {
            "vertical":    "┇",
            "horizontal":  "┅",
            "top-left":    "┏",
            "top-right":   "┓",
            "bottom-left": "┗",
            "bottom-right":"┛",
            "cross":       "╋",
            "tee-up":      "┻",
            "tee-down":    "┳",
            "tee-right":   "┣",
            "tee-left":    "┫"
        },
        "double-dashed": {
            "vertical":    "╏",
            "horizontal":  "╍",
            "top-left":    "┏",
            "top-right":   "┓",
            "bottom-left": "┗",
            "bottom-right":"┛",
            "cross":       "╋",
            "tee-up":      "┻",
            "tee-down":    "┳",
            "tee-right":   "┣",
            "tee-left":    "┫"
        },
        "quadruple-dashed": {
            "vertical":    "┋",
            "horizontal":  "┉",
            "top-left":    "┏",
            "top-right":   "┓",
            "bottom-left": "┗",
            "bottom-right":"┛",
            "cross":       "╋",
            "tee-up":      "┻",
            "tee-down":    "┳",
            "tee-right":   "┣",
            "tee-left":    "┫"
        }
    },
    "double": {
        "solid": {
            "vertical":    "║",
            "horizontal":  "═",
            "top-left":    "╔",
            "top-right":   "╗",
            "bottom-left": "╚",
            "bottom-right":"╝",
            "cross":       "╬",
            "tee-up":      "╩",
            "tee-down":    "╦",
            "tee-right":   "╠",
            "tee-left":    "╣"
        },
        "vertical-double-horizontal-single": {
            "vertical":    "║",
            "horizontal":  "─",
            "top-left":    "╓",
            "top-right":   "╖",
            "bottom-left": "╙",
            "bottom-right":"╜",
            "cross":       "╫",
            "tee-up":      "╨",
            "tee-down":    "╥",
            "tee-right":   "╟",
            "tee-left":    "╢"
        },
        "vertical-single-horizontal-double": {
            "vertical":    "│",
            "horizontal":  "═",
            "top-left":    "╒",
            "top-right":   "╕",
            "bottom-left": "╘",
            "bottom-right":"╛",
            "cross":       "╪",
            "tee-up":      "╧",
            "tee-down":    "╤",
            "tee-right":   "╞",
            "tee-left":    "╡"
        }
    }
}  # DATA STRUCTURE USED TO MAKE THE TABLE. (THESE ARE CALLED UNICODE BOX DRAWING CHARACTERS)

def tabulate(data,
             title=None,
             weight="light",
             style="solid",
             justify="center",
             padding=2):
    BxD=BoxDrawing[weight][style]
    #STRING ALL OBJECTS:
    data=[[str(item) for item in row] for row in data]

    #MEASURE MAX WIDTH PER COL:
    colWidths=[max([len(item) for item in col]) for col in zip(*data)]

    if(justify=="center"):
        data=[[item.center(width+padding) for item,width in zip(list(row),colWidths)] for row in data]
    elif(justify=="left"):
        data=[[item.ljust(width+padding) for item,width in zip(list(row),colWidths)] for row in data]
    elif(justify=="right"):
        data=[[item.rjust(width+padding) for item,width in zip(list(row),colWidths)] for row in data]
    header=data[0]
    data.pop(0)


    tabulated=[BxD["vertical"]+(BxD["vertical"].join(row))+BxD["vertical"] for row in data]


    header_cap=BxD["top-left"]+(BxD["tee-down"].join(BxD["horizontal"]*(width+padding) for width in colWidths))+BxD["top-right"]

    header_butt=BxD["tee-right"]+(BxD["cross"].join(BxD["horizontal"]*(width+padding) for width in colWidths))+BxD["tee-left"]

    table_butt=BxD["bottom-left"]+(BxD["tee-up"].join(BxD["horizontal"]*(width+padding) for width in colWidths))+BxD["bottom-right"]

    table=header_cap+"\n"+(BxD["vertical"]+BxD["vertical"].join(header)+BxD["vertical"]+"\n")+header_butt+"\n"+("\n".join(tabulated))+"\n"+table_butt

    
    if(title==None):
        return table
    else:
        table=(title.center(sum(colWidths)+(padding*len(colWidths))+(len(colWidths)+3)))+"\n"+table
    return table