
### The List:

- [ ] Fun one, how far does it run unaided?
- [ ] What if I validated the existing images (even on manifest existing) by a random sampling off of the scryfall api itself? Validation levels? (force, sample n, none)
- [ ] Script needs to update the manifest based on images (perhaps when generated too?)
- [ ] Layouts. Omit unnecessary ones. Write to the manifest all about doing it.
- [ ] Script does LEA well enough. I let it run without issue, only timed out because the laptop lost power. It could concievably run until the really complicated layouts, but yeah; the above.
- [ ] Logging is a best-guess, consider crafting some guidelines.
- [ ] What are `.pyc` files and what do I need to do with them?
- [ ] Test that the shared run configuration works on a fresh device.
Did this on the win10 box, and the run configuration is a little wonky, given that it's tied directly to where the interpreter lives on the device. Selecting the project interpreter and having it configured to work off that is probably the correct path. **update**: I've got this working kinda, there are some things that I consciously ignore about the usability though. Would be nice to work towards getting this to a place where someone else could conceivably do this, but this ties closely into overall project structure and should probably come after. Anyway, keep at it.

### The Done List:

- [x] Decide on python 3.6 vs **3.7**.
- [x] Expand manifest to include release date
- [x] Script should be ordered to work chronologically, so then there's a natural way to tell what's left to do (and what doesn't need to be updated)

### Readings on Structure:

https://docs.python-guide.org/writing/structure/

https://realpython.com/python-program-structure/
