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




# TABLE CLASS:
class Table:
    def __init__(self, data,
                 title=None,
                 padding=0,
                 weight="light",
                 style="solid",
                 justify="center"):
        if not isinstance(data,list):
            raise TypeError("Must be a 2D Python list.")
        else:
            length=len(data[0])
            for row in data:
                if(length==len(row)):
                    continue
                else:
                    raise ValueError("Inconsistent shape. Must be a 2D Python list.")
            self.data=[[str(item) for item in row] for row in data]
            self.title=title
            self.padding=padding
            self.weight=weight
            self.style=style
            self.justify=justify

    # ACCESSING ELEMENTS:
    def __getitem__(self, key):
        if not isinstance(key, tuple):
            raise TypeError("Must be a tuple of integer values.")
        else:
            row,col=key
            if (isinstance(row,int) and isinstance(col,int)):
                return self.data[row][col]
    def __setitem__(self, key, value):
        if not isinstance(key, tuple):
            raise TypeError("Must be a tuple of integer values.")
        else:
            row,col=key
            if (isinstance(row,int) and isinstance(col,int)):
                self.data[row][col]=str(value)
                return self
    
    # IN PLACE ROW APPEND:
    def appendRow(self, row):
        if not isinstance(row, list):
            raise ValueError("Must be a 1D Python list.")
        else:
            row=list(map(str,row))
            self.data.append(row)
            return self

    # IN PLACE COL APPEND:
    def appendCol(self, col):
        if not isinstance(col, list):
            raise ValueError("Must be a 1D Python list.")
        else:
            col=list(map(str,col))

            temp=[col for col in zip(*self.data)]
            self.data.clear()
            self.data.extend(temp)

            self.data.append(col)

            temp=[col for col in zip(*self.data)]
            self.data.clear()
            self.data.extend(temp)
            
            return self

    # STR-REPRESENTATION OF TABLE OBJECT:
    def __str__(self):
        BxD=BoxDrawing[self.weight][self.style]

        colWidths=[max([len(item)+self.padding for item in col])for col in zip(*self.data)]
        if (self.justify=="center"):
            fixed_data=[[item.center(width) for width,item in zip(colWidths,row)] for row in self.data]
        elif (self.justify=="left"):
            fixed_data=[[item.ljust(width) for width,item in zip(colWidths,row)] for row in self.data]
        elif (self.justify=="right"):
            fixed_data=[[item.rjust(width) for width,item in zip(colWidths,row)] for row in self.data]

        head=fixed_data[0]
        body=fixed_data[1:len(fixed_data)]

        header_cap=BxD["top-left"]+(BxD["tee-down"].join([BxD["horizontal"]*(width) for width in colWidths]))+BxD["top-right"]
        header=BxD["vertical"]+(BxD["vertical"].join(head))+BxD["vertical"]
        header_butt=BxD["tee-right"]+(BxD["cross"].join([BxD["horizontal"]*(width) for width in colWidths]))+BxD["tee-left"]

        table_body="\n".join([BxD["vertical"]+(BxD["vertical"].join(row))+BxD["vertical"] for row in body])
        table_butt=BxD["bottom-left"]+(BxD["tee-up"].join([BxD["horizontal"]*(width) for width in colWidths]))+BxD["bottom-right"]

        # MAKING THE TITLE:
        if(self.title==None):
            return "\n".join([header_cap,header,header_butt,table_body,table_butt])
        else:
            title_cap=BxD["top-left"]+(BxD["horizontal"].join([BxD["horizontal"]*(width) for width in colWidths]))+BxD["top-right"]

            main_title=BxD["vertical"]+self.title.center(sum(colWidths)+len(colWidths)-1)+BxD["vertical"]

            title_butt=BxD["bottom-left"]+(BxD["horizontal"].join([BxD["horizontal"]*(width) for width in colWidths]))+BxD["bottom-right"]
            return "\n".join([title_cap,main_title,title_butt,header_cap,header,header_butt,table_body,table_butt])


# TESTING THE CLASS:
smartphone_data = [
    ["Brand", "Model", "Storage", "Price"],
    ["Apple", "iPhone 17 Pro", "256GB", "$999"],
    ["Samsung", "Galaxy S26 Ultra", "512GB", "$1,299"],
    ["Google", "Pixel 10 Pro", "256GB", "$949"],
    ["OnePlus", "14 Ultra", "512GB", "$899"]
]

t_tech = Table(smartphone_data, title="Top Flagship Smartphones", padding=1, justify="center")
print(t_tech)
planet_data = [
    ["Planet", "Type", "Radius (km)", "Moons"],
    ["Mercury", "Terrestrial", "2,440", "0"],
    ["Venus", "Terrestrial", "6,051", "0"],
    ["Earth", "Terrestrial", "6,371", "1"],
    ["Mars", "Terrestrial", "3,389", "2"]
]

t_space = Table(planet_data, title="Inner Solar System", padding=1, justify="center")
print(t_space)