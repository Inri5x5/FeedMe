import React from 'react'
import Avatar from '@mui/material/Avatar';
import styles from './styles/LeftNavDashboard.module.css'
import Button from '@mui/material/Button';

const LeftNavDashboard = (props) => {
  // There are 3 buttons = "Saved",  "Rated", "Created"

  const clickButton = (button_name) => {
    props.setClickedButton(button_name)
  }

  const isClicked = (button_name) => {
    if (props.clickedButton === button_name) return true;
    return false;
  }

  return (

    <div className={styles.container}>
        <div className={styles.profile_container}>
            <Avatar
                alt="Remy Sharp"
                src="/static/images/avatar/1.jpg"
                sx={{ width: '15vw', height: '15vw' }}
            />
            <div className={styles.user_name}> Name </div>
        </div>
        <div>
            <button className={(isClicked("Saved")) ? styles.button_focus : styles.button} onClick={() => {clickButton("Saved")}}>Saved Recipes</button>
            <button className={(isClicked("Rated")) ? styles.button_focus : styles.button} onClick={() => {clickButton("Rated")}}>Rated Recipes</button>
            <button className={(isClicked("Created")) ? styles.button_focus : styles.button} onClick={() => {clickButton("Created")}}>My Recipes</button>
        </div>
    </div>
  )
}

export default LeftNavDashboard