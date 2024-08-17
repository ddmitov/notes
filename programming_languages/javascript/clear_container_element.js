// -*- coding: utf-8 -*-

function clearContainerElement (container) {
    while (container.firstChild) {
        container.removeChild(container.firstChild)
    }
}
