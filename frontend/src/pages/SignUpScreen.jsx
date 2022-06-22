import React from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';

export default function SignupScreen () {
    const navigate = useNavigate();
    return (
    <div className="signupContainer">
        Test SignUpScreen
        <Button onClick={() => navigate("/")}> HOME ! </Button>
        <Button onClick={() => navigate("/login")}> LOGIN ! </Button>
    </div>
    )
}