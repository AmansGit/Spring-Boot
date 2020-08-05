package com.aman.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HomeController {
	@RequestMapping("home")
//	@ResponseBody	//just print "return" string to web page.
//	public String home(HttpServletRequest req, HttpServletResponse res) {
//		HttpSession session = req.getSession();
//		String name = req.getParameter("name");
//		System.out.println("Are u there?? " + name);
//		session.setAttribute("name", name);
//		return "home";
//	}

	//		Without using Servelet-Request ---->

//	public String home(String name, HttpSession session) {
//		System.out.println("Are u there?? " + name);
//		session.setAttribute("name", name);
//		return "home";
//	}

	//		Using Model-View --------->

//	public ModelAndView home(@RequestParam("name") String myName) {
//		ModelAndView mv = new ModelAndView(); //ModelAndView is responsible to hold two things data and view name
//		mv.addObject("name", myName); 		// here data is hold
//		mv.setViewName("home");							// here view name is hold (home.jsp)
//		System.out.println("Are u there?? " + myName);
//		return mv;
//	}

	//		Accepting three diff values from client
	public ModelAndView home(Aman aman) {
		ModelAndView mv = new ModelAndView(); //ModelAndView is responsible to hold two things data and view name
		mv.addObject("obj", aman); 		// here data is hold
		mv.setViewName("home");							// here view name is hold (home.jsp)
		return mv;
	}
}