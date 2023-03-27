import React from "react";
import { IconButton } from '@mui/material';
import { Brightness4, Brightness7 } from "@mui/icons-material";

function ThemeToggle({ onToggleDarkMode, themeType }) {
  const handleToggleDarkMode = () => {
    onToggleDarkMode(); // call the callback function to update theme type
  };
  return (
    <div style={{
      position: "fixed",
      top: 0,
      right: 0,
      padding: "10px",
      zIndex: 9999,
    }}>
      <IconButton onClick={handleToggleDarkMode}>
        {themeType ? <Brightness7 /> : <Brightness4 />  }
      </IconButton>
    </div>
  );
}

export default ThemeToggle;