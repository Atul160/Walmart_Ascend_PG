import { combineReducers } from 'redux';
import contactsReducer from './contacts-reducer';
// all reducers shall be kept here as single source of truth 



export default combineReducers({
    contactsReducer
});
