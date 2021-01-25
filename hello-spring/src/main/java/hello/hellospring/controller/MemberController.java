package hello.hellospring.controller;

import hello.hellospring.domain.Member;
import hello.hellospring.service.MemberService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class MemberController {

    private final MemberService memberService;

//    @Autowired 생략 가능, 객체가 생성되려면 반드시 매개로 들어오는 객체가 존재해야 하므로 자동으로 생성된 후 주입된다.
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    // Home
    @GetMapping("/")
    public String loginForm() {
        return "loginForm";
    }

    // 회원등록 버튼 클릭시 회원등록 페이지를 리턴
    @GetMapping("/members/new")
    public String createMemberForm() {
        return "/members/createMemberForm";
    }

    // 회원을 실제 등록하는 기능
    @PostMapping("/members/new")
    public String create(MemberForm form) {
        Member member = new Member();

        member.setName(form.getName());

        memberService.join(member);

        return "redirect:/";
    }

    // 회원 조회
    @GetMapping("/members")
    public String list(Model model) {
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members);
        return "/members/memberList";
    }

}
