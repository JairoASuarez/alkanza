#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sept 15 2019
@author: Jairo Suarez
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer) -> None:
        """
        Attachs an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        """
        Detachs an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifies all observers about an event.
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class User(Subject):
    name = None
    _observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def test(self, name: str) -> None:
        self.name = name
        print("User: My name has just changed to: {}".format(self.name))
        self.notify()


class ConcreteObserver(Observer):
    def update(self, user: User) -> None:
        print("ConcreteObserver: Reacted to the event")


if __name__ == "__main__":
    example_user = User()
    concrete_observer = ConcreteObserver()
    example_user.attach(concrete_observer)
    example_user.test("Jairo")
    example_user.detach(concrete_observer)
    example_user.test("Alberto")
