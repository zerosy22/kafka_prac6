import React, { useState } from "react";
import { TextField, Paper, Button, Grid } from "@material-ui/core";
import axios from 'axios';
import Cookies from 'js-cookie';

function AddSignup(props) {
    const [setbxId, setSetbxId] = useState("");
    const [userEmail, setUserEmail] = useState("");
    const [userPwd, setUserPwd] = useState("");
    const [userName, setUserName] = useState("");
    const [userPhone, setUserPhone] = useState("");
    const [userSex, setUserSex] = useState("");
    const [userBirth, setUserBirth] = useState("");
    const [userAdult, setUserAdult] = useState("");
    const [userAdultKey, setUserAdultKey] = useState("");
    const [userLikeGenre, setUserLikeGenre] = useState("");
    const [userLikeVod, setUserLikeVod] = useState("");

    const onSetbxIdChange = (event) => {
        setSetbxId(event.target.value);
    };
    const onUserEmailChange = (event) => {
        setUserEmail(event.target.value);
    };
    const onUserPwdChange = (event) => {
        setUserPwd(event.target.value);
    };
    const onUserNameChange = (event) => {
        setUserName(event.target.value);
    };
    const onUserPhoneChange = (event) => {
        setUserPhone(event.target.value);
    };
    const onUserSexChange = (event) => {
        setUserSex(event.target.value);
    };
    const onUserBirthChange = (event) => {
        setUserBirth(event.target.value);
    };
    const onUserAdultChange = (event) => {
        setUserAdult(event.target.value);
    };
    const onUserAdultKeyChange = (event) => {
        setUserAdultKey(event.target.value);
    };
    const onUserLikeGenreChange = (event) => {
        setUserLikeGenre(event.target.value);
    };
    const onUserLikeVodChange = (event) => {
        setUserLikeVod(event.target.value);
    };

    const onSubmit = (event) => {
        event.preventDefault();
        const user = {
            SETBX_ID: setbxId,
            USER_EMAIL: userEmail,
            USER_PWD: userPwd,
            USER_NAME: userName,
            USER_PHONE: userPhone,
            user_sex: userSex,
            USER_BIRTH: userBirth,
            USER_ADULT: userAdult,
            USER_ADULT_KEY: userAdultKey,
            USER_LIKE_GENRE: userLikeGenre,
            USER_LIKE_VOD: userLikeVod,
        };
    //     const user = {
    //         setbxId,
    //         userEmail,
    //         userPwd,
    //         userName,
    //         userPhone,
    //         userSex,
    //         userBirth,
    //         userAdult,
    //         userAdultKey,
    //         userLikeGenre,
    //         userLikeVod,
    //     };
    //     props.add(user);
    //     setSetbxId("");
    //     setUserEmail("");
    //     setUserPwd("");
    //     setUserName("");
    //     setUserPhone("");
    //     setUserSex("");
    //     setUserBirth("");
    //     setUserAdult("");
    //     setUserAdultKey("");
    //     setUserLikeGenre("");
    //     setUserLikeVod("");
    // }
        // App.js에서 전달할 함수를 호출해서 데이터를 삽입
        props.add(user);
        
        axios.post('http://127.0.0.1:8000/signup_cud/', user, {
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken')
            }
        })
        .then(response => {
            console.log(response.data);
            setSetbxId("");
            setUserEmail("");
            setUserPwd("");
            setUserName("");
            setUserPhone("");
            setUserSex("");
            setUserBirth("");
            setUserAdult("");
            setUserAdultKey("");
            setUserLikeGenre("");
            setUserLikeVod("");
            alert("저장에 성공했습니다.");
        })
        .catch(error => {
            console.error('There was an error!', error);
            if (error.response && error.response.data && error.response.data.error) {
                alert(error.response.data.error);
            } else {
                alert("저장을 실패했습니다.");
            }
        });
    };

    return (
        <Paper style={{ margin: 16, padding: 16 }}>
             <Grid container spacing={3}>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="SETBX_ID"
                        value={setbxId}
                        onChange={(e) => setSetbxId(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_EMAIL"
                        value={userEmail}
                        onChange={(e) => setUserEmail(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_PWD"
                        type="password"
                        value={userPwd}
                        onChange={(e) => setUserPwd(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_NAME"
                        value={userName}
                        onChange={(e) => setUserName(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_PHONE"
                        value={userPhone}
                        onChange={(e) => setUserPhone(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_SEX"
                        value={userSex}
                        onChange={(e) => setUserSex(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_BIRTH"
                        type="date"
                        value={userBirth}
                        onChange={(e) => setUserBirth(e.target.value)}
                        fullWidth
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_ADULT"
                        value={userAdult}
                        onChange={(e) => setUserAdult(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_ADULT_KEY"
                        value={userAdultKey}
                        onChange={(e) => setUserAdultKey(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_LIKE_GENRE"
                        value={userLikeGenre}
                        onChange={(e) => setUserLikeGenre(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={6} item>
                    <TextField
                        label="USER_LIKE_VOD"
                        value={userLikeVod}
                        onChange={(e) => setUserLikeVod(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid xs={12} md={12} item>
                    <Button
                        fullWidth
                        color="secondary"
                        variant="outlined"
                        onClick={onSubmit}
                    >
                        Submit
                    </Button>
                </Grid>
            </Grid>
        </Paper>
    );
}

export default AddSignup;
