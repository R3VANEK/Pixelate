class PixelBox:

    size = 0
    avgcolor = ()
    palette = [
        "bla"

    ]

    def __init__(self, size):
        self.size = size

    # Właściwe kolorowanie z użyciem avg color
    def paintColor(self, pixels_map, j, i):

        for x in range(j, j + self.size):
            for y in range(i, i + self.size):
                pixels_map[x,y] = self.avgcolor

    def setAvgColor(self, pixels_map, j, i):

        r = 0
        g = 0
        b = 0
        count = 0

        for x in range(j, j + self.size):
            for y in range(i, i + self.size):
                r_calc, g_calc, b_calc = pixels_map[x,y]
                r+=r_calc
                g+=g_calc
                b+=b_calc
                count+=1

        #avgcolor bez patrzenia na palete
        self.avgcolor = ((r//count), (g//count), (b//count)) 

        most_accurate = () 
        max_score = 500000 
        current_score = 0
        for i in range(len(self.palette)):
            r_average, g_average, b_average = self.avgcolor
            r_palette, g_palette, b_palette = self.palette[i]

            current_score = abs(r_average - r_palette) + abs(g_average - g_palette) + abs(b_average - b_palette)
            if current_score < max_score:
                max_score = current_score
                most_accurate = self.palette[i]

        self.avgcolor = most_accurate
