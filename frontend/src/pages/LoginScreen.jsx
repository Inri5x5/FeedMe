import React from 'react'
import { useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';

export default function LoginScreen () {
    const navigate = useNavigate();
    
    return (
        <div className="loginContainer">
            Test LoginScreen
            <Button onClick={() => navigate("/")}> HOME ! </Button>
            <Button onClick={() => navigate("/register")}> SIGN UP ! </Button>
        </div>
        )
}