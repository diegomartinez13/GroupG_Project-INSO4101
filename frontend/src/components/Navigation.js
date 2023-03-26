import React from 'react';
import { NavLink } from 'react-router-dom';

function Navigation() {
  return (
    <md-navigation-bar>
      <ul>
        <li>
          <NavLink to="/">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/events">Events</NavLink>
        </li>
        <li>
          <NavLink to="/recycling-centers">Recycling Centers</NavLink>
        </li>
        <li>
          <NavLink to="/profile">Profile</NavLink>
        </li>
        <li>
          <NavLink to="/forum">Forum</NavLink>
        </li>
      </ul>
      </md-navigation-bar>
  );
}

export default Navigation;