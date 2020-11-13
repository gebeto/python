import React from 'react';

import { StatefulInput } from 'baseui/input';
import { Button, SIZE } from "baseui/button";


export const Auth = () => {
	const handleClick = React.useCallback(() => {
		window.location.href = "/auth";
	}, []);

	return (
		<React.Fragment>
			<Button
				size={SIZE.large}
				onClick={handleClick}
			>Authorize</Button>
		</React.Fragment>
	);
}
