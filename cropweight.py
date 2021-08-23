class CropRatio:

    def __init__(self):
        self._crops = {}
        self._total_weight = 0

    def add(self, name, crop_weight):
        curr_crop_weight = 0
        curr_crop_weight = curr_crop_weight + crop_weight
        
        self._total_weight += curr_crop_weight
        
        if not name in self._crops:
            self._crops[name] = crop_weight
        else: self._crops[name] = self._crops[name] + crop_weight
        
    def proportion(self, name):
        if(self._total_weight!=0):
            return self._crops[name]/self._total_weight
        else: return 0

#To see the output, uncomment the lines below:
crop_ratio = CropRatio()
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)

print(crop_ratio.proportion('Wheat'))