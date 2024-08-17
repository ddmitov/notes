// -*- coding: utf-8 -*-

function insertLetterTextArea (targetElementId, letter) {
  var targetElement = document.getElementById(targetElementId);
  const [start, end] = [targetElement.selectionStart, targetElement.selectionEnd];

  targetElement.setRangeText(letter, start, end, 'end');
}
