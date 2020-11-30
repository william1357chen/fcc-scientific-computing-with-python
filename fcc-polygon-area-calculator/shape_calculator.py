class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return "{}\n".format("*" * self.width) * (self.height) 

    def get_amount_inside(self, other):
        amount = 0
        self_width, self_height = self.width, self.height
        other_width, other_height = other.width, other.height

        top_to_bottom = True
        while top_to_bottom:
            if self_height >= other_height:
                left_to_right = True
                other_width = other.width
                while left_to_right:
                    if self_width >= other_width:
                        amount += 1
                        other_width += other.width

                    else:
                        left_to_right = False
                other_height += other.height
            else:
                top_to_bottom = False
        return amount
    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_side(self, length):
        self.set_width(length)

    def set_height(self, length):
        super().set_height(length)
        super().set_width(length)

    def set_width(self, length):
        super().set_height(length)
        super().set_width(length)

    def __repr__(self):
        return "Square(side={})".format(self.width)
    
