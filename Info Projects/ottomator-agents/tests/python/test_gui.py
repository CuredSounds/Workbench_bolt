import pytest
from project_starter_gui.gui_main import ProjectStarterGUI

def test_gui_initialization():
    """Test that GUI initializes without errors."""
    gui = ProjectStarterGUI()
    assert gui.window is not None
    gui.window.close()

def test_layout_creation():
    """Test that layout contains all necessary elements."""
    gui = ProjectStarterGUI()
    
    # Check for main components in layout
    layout_str = str(gui.layout)
    assert 'project_name' in layout_str
    assert 'project_location' in layout_str
    assert 'terraform' in layout_str
    assert 'kubernetes' in layout_str
    assert 'scraping' in layout_str
    assert 'ml' in layout_str
    
    gui.window.close() 