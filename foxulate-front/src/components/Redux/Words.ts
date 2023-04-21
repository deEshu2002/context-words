import { PayloadAction, createSlice } from "@reduxjs/toolkit";

export interface WordsState{
    words: string[],
}

const initialState:WordsState = {
    words:[
    "ease",
    "creativity",
    "cooperation",
    "changes",
    "epitome",
    "vulnerable",
    "exhilarating",
  ]
};

export const ChangeWordSlice = createSlice({
    name: 'changeWords', 
    initialState,
    reducers: {
        updateWords: (state, action:PayloadAction<WordsState>) => {
            for(let i = 0; i < state.words.length; i++){
                state.words[i] = action.payload.words[i] as string;
            }
        }
    }
});

export const { updateWords } = ChangeWordSlice.actions;

export default ChangeWordSlice.reducer;