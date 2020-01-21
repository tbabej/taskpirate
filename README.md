Taskpirate
----------

Taskpirate is a pluggable system for TaskWarrior python hooks.

Why?
----

Simpler hooks:

    def hook_example(task):
        task['description'] += "changed by a hook"

The above is fully working example, no more boilerplate needed.

Much faster execution time in case of multiple hooks (read the more details section).

Install
-------

You'll need tasklib as a dependency:

    pip install --user git+git://github.com/tbabej/tasklib@develop

Then you need to save ```on-add-pirate``` and ```on-modify-pirate``` from this repository into ~/.task/hooks/.

After that, you can just clone any taskpirate-enabled hook as a subfolder into ~/.task/hooks/:

    git clone https://github.com/tbabej/task.default-date-time ~/.task/hooks/default-date-time/

How to write a taskpirate hook
------------------------------

In your hook's repository, any file matching ```pirate_add*.py``` will be searched for hooks in on-add event. In the same sense, any file matching ```pirate_mod*.py``` will be searched for hooks in on-modify event.

Now, the pirate_add_example.py might look as follows:

    def hook_example(task):
        task['description'] += "changed by a hook"

Any function in pirate_add_example that is called ```hook_*``` will be considered as a hook in on-add event. It will be passed the ```Task``` object corresponding to the current state of the task being added (as modified by the previous hooks).

More details
------------

TaskWarrior hooks are intended to be simple, but they involve writing some boilerplate code (parsing/formatting json). To allow users to write dead simple code, they can leverage tasklib.

Using tasklib simplifies things a lot, however, it's not a super-lightweight - usage of tasklib can slow down the hook by as much as 30-50ms (usual python hook can probably run in under 40ms), since it imports multiple libraries.

This becomes a problem when user has multiple tasklib-based hooks, since the import time adds up.

Also, note that taskpirate with arbitrary number of hooks will be most likely faster than 2-3 regular python hooks.

Example hooks
-------------

You can look into my ```task.default-date-time``` or ```task.shift-recurrence``` hooks.
