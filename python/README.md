
Python 3.7.3

### The List:

- [ ] Having create_set_dir check for the images dir is fine for now, but it would be nice if this dir could be committed to git somehow.
- [ ] Now that I'm on VSCode, I'm not really digging how the script ungracefully fails when I'm not in the right directory.
- [ ] manifest.csv needs headers, I'm already forgetting which columns are what.
- [ ] When a manifest is generated, it should determine how many images exist in each set directory to avoid never recording an image count.
- [ ] What if I validated the existing images (even on manifest existing) by a random sampling off of the scryfall api itself? Validation levels? (force, sample n, none)
- [ ] Layouts. Omit unnecessary ones. Write to the manifest all about doing it.
- [ ] Logging is a best-guess, consider crafting some guidelines.
- [ ] Test that the shared run configuration works on a fresh device.
Did this on the win10 box, and the run configuration is a little wonky, given that it's tied directly to where the interpreter lives on the device. Selecting the project interpreter and having it configured to work off that is probably the correct path. **update**: I've got this working kinda, there are some things that I consciously ignore about the usability though. Would be nice to work towards getting this to a place where someone else could conceivably do this, but this ties closely into overall project structure and should probably come after. Anyway, keep at it.

### The Done List:

- [x] What are `.pyc` files and what do I need to do with them? -> Don't commit.
- [x] Fun one, how far does it run unaided? -> @ INV split cards.
- [x] Decide on python 3.6 vs **3.7**.
- [x] Expand manifest to include release date
- [x] Script should be ordered to work chronologically, so then there's a natural way to tell what's left to do (and what doesn't need to be updated)
- [x] Script needs to update the manifest based on images 

### Readings

#### Structure:
- https://docs.python-guide.org/writing/structure/
- https://realpython.com/python-program-structure/

#### .pyc Files:
- https://stackoverflow.com/questions/2998215/if-python-is-interpreted-what-are-pyc-files
- https://coderwall.com/p/wrxwog/why-not-to-commit-pyc-files-into-git-and-how-to-fix-if-you-already-did
