# -*- coding: utf-8 -*-

import os
import random

CH = 100  # the usual dilution ration
science = False
water_memory = True


class Homeo:
    """class doc"""

    def __init__(self, _file, solvent=None, ntimes=None):
        """method doc"""
        self._file = _file
        self.solvent = solvent
        self.ntimes = ntimes
        pass

    def dilute(self, words, solvent="~"):
        """Dilute a list of words into a solvent.

        After this step the solvent is not mixed with the original product. You need to "dynamize" it afterwards."""
        if type(words) is not list:
            raise TypeError("words must be a list.")
        if type(solvent) is not str:
            raise TypeError("solvent must be a string.")

        [words.append(solvent) for _ in range((CH - 1) * len(words))]

        return words

    def dynamize(self, words, ntimes=2):
        """Dynamize a list of words (i.e. shake very hard).

        Default shake number is 2 because 2 >> 0."""
        if type(words) is not list:
            raise TypeError("words must be a list.")
        if type(ntimes) is not int:
            raise TypeError("ntimes must be a int.")
        if ntimes <= 0:
            raise ValueError("ntimes must be > 0.")
        if science:
            raise ValueError("This is not science.")

        [random.shuffle(words) for _ in range(ntimes)]

        return words

    def homeify(self, ch=1):
        """Does the magic to your text file."""
        filename, file_extension = os.path.splitext(self._file)
        homeo_file = "{}_CH{}{}".format(filename, ch, file_extension)

        try:
            with open(self._file, 'r') as infile, open(homeo_file, 'w') as outfile:
                for line in infile:
                    words = line.split()
                    for _ in range(ch):
                        if science:
                            break
                        if self.solvent:
                            words = self.dilute(words, solvent=self.solvent)  # Dilute by 1CH
                        else:
                            words = self.dilute(words)
                        if self.ntimes:
                            words = self.dynamize(words, ntimes=self.ntimes)  # Energize
                        else:
                            if self.ntimes:
                                words = self.dynamize(words)
                        words = words[:len(words) // CH]  # Keep the initial volume
                    outfile.write("{}\n".format(" ".join(words)))
        except IOError as e:
            print('Operation failed (what did you expect from homeopathy?): {}'.format(e.strerror))


if __name__ == "__main__":
    print("Open your eyes ladies and gentlemen, for I am going to dilute the sh*t out of this sample text!")
    file = "sample_data/Alice's Adventures in Wonderland.txt"
    text = Homeo(file, solvent="~", ntimes=2)
    text.homeify(ch=1)
    print("1CH homeopathic text done.")
