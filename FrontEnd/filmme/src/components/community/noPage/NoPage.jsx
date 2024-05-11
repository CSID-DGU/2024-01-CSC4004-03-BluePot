import React from "react";
import { styled, keyframes } from "styled-components";

const fadeInAnimation = keyframes`
    from {
        opacity: 0;
        transform: translateY(-2rem);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
`;

export const PagingNoPage = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 3rem;
    font-weight: 500;
    animation: ${fadeInAnimation} 0.5s ease-in-out;
`;

export const PagingNoPageIcon = styled.img`
    width: 10rem;
    height: 7rem;
    margin: 7rem 0rem 4rem 0rem;
`;

function NoPage() {
    return (
        <PagingNoPage>
        <PagingNoPageIcon />
        게시글이 아직 없습니다!
        </PagingNoPage>
    );
}

export default NoPage;